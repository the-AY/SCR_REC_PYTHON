# This code basically takes number of screenshots and combines it together to make a video file and save it as recording.avi 
# Used python library Numpy as an array to store the screenshots
# importing the required packages
import pyautogui
import numpy as np
# Specify resolution of the Display
resolution = (1920, 1080)

#  video codec Standard
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file this file will be saved in the current code directory
filename = "Recording.avi"

# Current frame rate ,change if there are lags in the recording (Please test this before recording)
fps = 60.0


# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live Screen", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live Screen", 480, 270)

while True:
	# Take screenshot using PyAutoGUI
	img = pyautogui.screenshot()

	# Convert the screenshot to a numpy array
	frame = np.array(img)

	# Convert it from BGR(Blue, Green, Red) to
	# RGB(Red, Green, Blue)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Write it to the output file
	out.write(frame)
	
	# Optional: Display the recording screen
	cv2.imshow('Live Screen', frame)
	
	# Stop recording when we press 'q'
	if cv2.waitKey(1) == ord('q'):
		break

out.release()

# Destroy all windows
cv2.destroyAllWindows()
