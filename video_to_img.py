import cv2
import os

files = os.listdir("kulit-sehat")
print(files)
count = 0
for file in files:
    print(file)
    vidcap = cv2.VideoCapture("kulit-sehat/" + file)
    success, image = vidcap.read()
    while success:
        cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file
        success, image = vidcap.read()
        print("Read a new frame: ", success)
        count += 1
    else:
        print("not success")
