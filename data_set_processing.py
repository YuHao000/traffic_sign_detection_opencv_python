import numpy as np
import cv2
import os

def generate_processed_img(img_path):
    img = cv2.imread(img_path)
    output_img = img.copy()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 75)

    if circles is None: return None

    circles = np.round(circles[0, :]).astype("int")
    x, y, r = max(circles, key = lambda x : x[2])

    output_img = output_img[y - r : y + r, x - r : x + r]
    return output_img

def generate_data_set():
    os.mkdir("gen")
    sign_list = os.listdir(".")
    for i, sign_file in enumerate(sign_list):
        if '.png' in sign_file:
            path = "./{}".format(sign_file)
            print(path)
            img = generate_processed_img(path)
            if img is None: continue
            success = cv2.imwrite("./gen/{}.png".format(i), img)
            if not success: os.remove("./gen/{}.png".format(i))

generate_data_set()