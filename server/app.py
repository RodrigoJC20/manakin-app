import cv2
import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
from removebg import RemoveBg

load_dotenv()

REMOVEBG_API_KEY = os.getenv("REMOVEBG_API_KEY")
GOOEY_API_KEY = os.getenv("GOOEY_API_KEY")


app = Flask(__name__)

rmbg = RemoveBg(REMOVEBG_API_KEY, "error.log")


@app.route("/")
def root():
	return render_template('home.html')


@app.route("/create_file", methods=["POST"])
def create_file():
	foreground = request.files.get("foreground")
	background = request.files.get("background")
	fg_name = foreground.filename
	bg_name = background.filename
	foreground.save(fg_name)
	background.save(bg_name)

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
	cv2.imwrite("static/" + bg_name, bg)
	return render_template("picture.html", filename=bg_name)  # FileResponse(bg_name)


# @app.route("/generate_image", methods=["POST"])
# def generate_image(data: Dict):
# 	first_prompt = "a wide angle street level photo of a busy street in New York, Mumbai, 4k, 8k, UHD"
# 	second_prompt = "a wide angle of a busy street in Manhattan, Mumbai, 4k, 8k, UHD"
# 	prompts = data.get("prompts", [first_prompt, second_prompt])
# 	# payload = {
# 	# 	"animation_prompts": [
# 	# 		{"frame": 0, "prompt": prompts[0],},
# 	# 		{"frame": 10, "prompt": prompts[1]},
# 	# 	]
# 	# }
# 	#
# 	# response = requests.post(
# 	# 	"https://api.gooey.ai/v2/DeforumSD/",
# 	# 	headers={
# 	# 		"Authorization": f"Bearer {GOOEY_API_KEY}"
# 	# 	},
# 	# 	json=payload,
# 	# )
#
# 	# output_video = response.json()['output']['output_video']
#
#
# 	output_video_url = ("https://storage.googleapis.com/dara-c1b52.appspot.com/daras_ai/media/41b4fbce-2042-11ef-9ff3"
# 	                    "-02420a00016d/gooey.ai%20animation%20frame%200%20prompt%20a%20wide%20angle%20s...ngle%20of%20a"
# 	                    "%20busy%20street%20in%20Shibuya%20Tokyo%204k%208k%20UHD.mp4")
# 	download_path = "downloaded_video.mp4"
# 	output_path = "final_video.mp4"
# 	overlay_image_path = "dp.jpeg_no_bg.png"
#
#
# 	def download_video(url, file_path):
# 		response = requests.get(url, stream=True)
#
#
# 	with open(file_path, 'wb') as file:
# 		for chunk in response.iter_content(chunk_size=8192):
# 			file.write(chunk)
# 	print(f"Video downloaded to {file_path}")
#
# 	download_video(output_video_url, download_path)
#
#
# 	def add_image(video_path):
# 		video = cv2.VideoCapture(video_path)
# 		overlay_image = cv2.imread(overlay_image_path)
#
# 		width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# 		height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 		fps = int(video.get(cv2.CAP_PROP_FPS))
#
# 		overlay_x = (width - overlay_image.shape[1]) // 2
# 		overlay_y = (height - overlay_image.shape[0]) // 2
#
# 		out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
#
# 		while True:
# 			ret, frame = video.read()
# 			if not ret:
# 				break
#
# 			overlay = frame.copy()
#
# 			mask = cv2.cvtColor(overlay_image, cv2.COLOR_BGR2GRAY)
# 			ret, mask = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)
# 			inv_mask = cv2.bitwise_not(mask)
#
# 			roi = overlay[overlay_y:overlay_y + overlay_image.shape[0], overlay_x:overlay_x + overlay_image.shape[1]]
# 			overlay_image_resized = cv2.resize(overlay_image, (roi.shape[1], roi.shape[0]))
# 			overlay = cv2.bitwise_and(roi, roi, mask=inv_mask)
# 			overlay_image_with_alpha = cv2.bitwise_and(overlay_image_resized, overlay_image_resized, mask=mask)
# 			roi_final = cv2.add(overlay, overlay_image_with_alpha)
# 			overlay = overlay_image
#
# 			# Blend the overlay with the frame
# 			alpha = 0.01
# 			frame[overlay_y:overlay_y + overlay_image.shape[0],
# 			overlay_x:overlay_x + overlay_image.shape[1]] = cv2.addWeighted(roi, alpha, roi_final, 1 - alpha, 0)
#
# 			out.write(frame)
# 		out.release()
# 		video.release()
# 		add_image(download_path)
# 		print(f"Processed video saved as {output_path}")
#
#
# 	return output_path
