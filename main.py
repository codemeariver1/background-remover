import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

# Open the webcam
capture = cv2.VideoCapture(0)

# Set frame
capture.set(3, 640) # Width
capture.set(4, 488) # Height

# Increase the frame rate
capture.set(cv2.CAP_PROP_FPS, 60)

# Create SelfiSegmentation object
segmentor = SelfiSegmentation()

# Get FPS
fps_reader = cvzone.FPS()

# Import single background image
# img_bg = cv2.imread("Images/room-on-fire-resized.jpeg")

# List all the images in the named folder
list_img = os.listdir("Images")
print(list_img)
# Store the list of images in a list
img_list = []
for img_path in list_img:
    img = cv2.imread(f'Images/{img_path}')
    img_list.append(img)
print(len(img_list))

index_img = 5

while True:
    # Get the image
    success, img = capture.read()

    # Run the segmentor
    img_out = segmentor.removeBG(img, img_list[index_img], threshold=0.62)

    # Stack the images and display the FPS
    img_stacked = cvzone.stackImages([img, img_out], 2, 1)
    fps, img_stacked = fps_reader.update(img_stacked, color=(50, 255, 0))

    print(index_img)

    # Show the image
    cv2.imshow("Look mom I'm on TV!", img_stacked)

    # Ability to change the background image while opened
    key = cv2.waitKey(1)
    if key == ord('a'):
        if index_img > 0:
            index_img -= 1
    elif key == ord('d'):
        if index_img < len(img_list) - 1:
            index_img += 1
    elif key == ord('q'):
        break
