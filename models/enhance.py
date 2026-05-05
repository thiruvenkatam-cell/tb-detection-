import cv2
from models.enhancement import enhance

img = cv2.imread("data/images/sample.png", 0) / 255.0
out = enhance(img)

cv2.imwrite("output_enhanced.png", out*255)
