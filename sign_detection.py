import cv2
import numpy as np
#cap = cv2.VideoCapture('‪test4.mp4')

def extract_roi(image):
    # output = cv2.imread("img/021.jpg")
    #cv2.imshow("frame",img)
    h, w = image.shape[:2]
    #imgResult = cv2.CreateImage((w,h),img.depth,1)
    imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("niveau de gris",gray)
    imagehsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #cv2.imshow("HSV",hsv)
    
    imagetraitement = image.copy()
    lower_red = np.array([35,80,115])
    upper_red = np.array([255,255,255])
    imagegray = cv2.inRange(imagehsv, lower_red, upper_red)
    cv2.imshow("rouge",imagegray)
    imagetraitement = cv2.cvtColor(imagegray, cv2.COLOR_GRAY2BGR)
    cv2.imshow("gray to rgb",imagetraitement)
    #gray = cv2.rectangle(gray,(0,0),(w//2,h//2),120,3)
    #gray2 = gray[0:h//2,0:w//2]
    # cv2.imshow("rect",gray2)
    imagegray1=imagegray.copy()
    circles = cv2.HoughCircles(imagegray1,cv2.HOUGH_GRADIENT,2,200,param1=10,param2=10,minRadius=1,maxRadius=200)

    if circles is None: return None

	# convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")
    x,y,r = max(circles, key=lambda x: x[2])
    
    output = image.copy()
    output = output[(y+r-2*r):(y+r), (x-r):(x-r+2*r)]
    cv2.circle(image,(x,y),r,120,2)
    cv2.imshow("cercle",image)
    return output, x, y, r