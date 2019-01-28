# from sign_detection import extract_roi
from detect_circles import extract_roi
from classification import training, getLabel, SVM
import cv2
import numpy as np


textLables = ["not defined", "50", "80", "70", "15", "5", "60", "40", "30"]

# video_cap = cv2.VideoCapture(0)
video_cap = cv2.VideoCapture("jarab.avi")

model = training()

# model = SVM()
# model.load('data_svm.dat')

while True:
    if not video_cap.isOpened():
        print("error: video capture is not opened")
        break
    ret, frame = video_cap.read()

    if not ret:
        print("error: failed to read frame")
        break

    frame = cv2.resize(frame, (640, 480))

    ret = extract_roi(frame)
    
    if ret is None:
        print("error: failed to extract roi")
        continue

    roi, x, y, r = ret

    label = textLables[getLabel(model, roi)]

    print(label)

    cv2.rectangle(frame, (x - r, y - r), (x + r, y + r), (0, 255, 255), 3)

    cv2.imshow("", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

video_cap.release()