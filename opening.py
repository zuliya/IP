import erosion
import dilation
import cv2
import sys


def opening():
    # read image using erosion
    img = erosion.readImg()
    # Dilate image then Erode image
    finalImg =  dilation.dilation(erosion.erosion(img))
    cv2.imwrite(sys.argv[2], finalImg)

if __name__== "__main__":
    opening()
