import cv2

def preprocess(image_path):
    img = cv2.imread(image_path, 0)
    img = cv2.resize(img, (512, 512))
    img = img / 255.0
    return img
