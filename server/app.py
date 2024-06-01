import cv2
from typing import List
from typing import Dict
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import requests
from server.server_secrets import REMOVEBG_API_KEY
from server.server_secrets import GOOEY_API_KEY
import os
import numpy as np
app = FastAPI()

from removebg import RemoveBg

rmbg = RemoveBg(REMOVEBG_API_KEY, "error.log")


@app.get("/")
async def root():
	return {"Hello": "World"}


@app.post("/create_file")
async def create_upload_file(foreground: UploadFile, background: UploadFile):
	fg_name = foreground.filename
	bg_name = background.filename
	contents = foreground.file.read()
	with open(foreground.filename, "wb") as f:
		f.write(contents)
	contents = background.file.read()
	with open(background.filename, "wb") as f:
		f.write(contents)
	bg_fg_name = fg_name + "_no_bg.png"
	if not os.path.exists(bg_fg_name):
		rmbg.remove_background_from_img_file(fg_name)
	fg_name = fg_name + "_no_bg.png"

	fg = cv2.imread(fg_name)  # foreground
	bg = cv2.imread(bg_name)  # background

	row_length = bg.shape[0] // 2
	col_length = bg.shape[1] // 2  # final image shape shoudl be (row_length, col_length)

	dims = (col_length, row_length)

	stretch_near = cv2.resize(fg, dims, interpolation=cv2.INTER_LINEAR)

	center = (bg.shape[0] // 2, bg.shape[1] // 2)  # image center
	left = center[0] - (row_length // 2)
	up = center[1] - (col_length // 2)

	original_bg = bg[left:left + stretch_near.shape[0], up:up + stretch_near.shape[1]]
	bg[left:left + stretch_near.shape[0], up:up + stretch_near.shape[1]] = (stretch_near == 0) * original_bg + (stretch_near != 0) * stretch_near
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
