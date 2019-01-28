# USAGE

# import the necessary packages
import numpy as np
import time
import cv2

# def LaplacianOfGaussian(image):
#     LoG_image = cv2.GaussianBlur(image, (7,7), 0)           # paramter 
#     gray = cv2.cvtColor( LoG_image, cv2.COLOR_BGR2GRAY)
#     LoG_image = cv2.Laplacian( gray, cv2.CV_8U,3,3,2)       # parameter
#     LoG_image = cv2.convertScaleAbs(LoG_image)
#     return LoG_image
    
# def binarization(image):
#     thresh = cv2.threshold(image,30,255,cv2.THRESH_BINARY)[1]
#     #thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
#     return thresh

# def preprocess_image(image):
#     # image = constrastLimit(image)
#     image = LaplacianOfGaussian(image)
#     image = binarization(image)
#     return image

 # captures image# displays captured image

	# Stream on
def extract_roi(image):
	output = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# gray = preprocess_image(image)
	# gray = binarization(gray)

	cv2.imshow("gray", gray)

	# detect circles in the image
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 75)
	# ensure at least some circles were found
	if circles is None: return None

	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles

	#find max radius
	x,y,r = max(circles, key=lambda x: x[2])
	output = output[(y+r-2*r):(y+r), (x-r):(x-r+2*r)]	

	return output, x, y, r
	
