import cv2
from matplotlib import pyplot as plt
import numpy
img = cv2.imread('bird.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
