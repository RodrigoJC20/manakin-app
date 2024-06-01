from rembg import remove
from PIL import Image
import cv2
from typing import List
from typing import Dict
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import requests
from server_secrets import REMOVEBG_API_KEY
from server_secrets import GOOEY_API_KEY
app = FastAPI()

from removebg import RemoveBg

rmbg = RemoveBg(REMOVEBG_API_KEY, "error.log")

@app.post("/create_file")
async def create_upload_file(files: List[UploadFile] = File(...)):
	foreground, background = files
	fg_name = foreground.filename
	bg_name = background.filename
	contents = foreground.file.read()
	with open(foreground.filename, "wb") as f:
		f.write(contents)
	contents = background.file.read()
	with open(background.filename, "wb") as f:
		f.write(contents)
	rmbg.remove_background_from_img_file(fg_name)
	fg_name = fg_name + "_no_bg.png"
	fg = cv2.imread(fg_name)
	bg = cv2.imread(bg_name)
	row_length = bg.shape[0] // 4
	col_length = bg.shape[1] // 4
	dims = (bg.shape[0] // 4, bg.shape[1] // 4)

	stretch_near = cv2.resize(fg, dims, interpolation=cv2.INTER_LINEAR)
	center = (bg.shape[1] // 2, bg.shape[0] // 2)
	row_slice = slice(center[0] - row_length // 2, center[0] + row_length // 2)
	col_slice = slice(center[1] - col_length // 2, center[1] + col_length // 2)
	bg[row_slice, col_slice] = stretch_near
	cv2.imwrite(fg_name, fg)
	cv2.imwrite(bg_name, bg)
	return FileResponse(bg_name)


@app.post("/generate_image")
async def generate_image(data: Dict):
	first_prompt = "a wide angle street level photo of a busy street in Versova, Mumbai, 4k, 8k, UHD"
	second_prompt = "a wide angle street level photo of a busy street in Versova, Mumbai, 4k, 8k, UHD"
	prompts = data.get("prompts", [first_prompt, second_prompt])
	payload = {
		"animation_prompts": [
			{"frame": 0, "prompt": prompts[0],},
			{"frame": 10, "prompt": prompts[1]},
		]
	}

	response = requests.post(
		"https://api.gooey.ai/v2/DeforumSD/",
		headers={
			"Authorization": f"Bearer {GOOEY_API_KEY}"
		},
		json=payload,
	)
	return response.json()['output']['output_video']
