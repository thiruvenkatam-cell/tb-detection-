import cv2
import numpy as np

def decompose(image):
    lf = cv2.GaussianBlur(image, (15,15), 0)
    hf = image - lf
    mf = image - (lf + hf)
    return lf, mf, hf

def enhance(image):
    lf, mf, hf = decompose(image)

    alpha, beta, gamma = 0.5, 1.0, 1.5
    enhanced = alpha*lf + beta*mf + gamma*hf

    mean = np.mean(enhanced)
    std = np.std(enhanced)

    normalized = (enhanced - mean) / (std + 1e-8)
    return normalized
