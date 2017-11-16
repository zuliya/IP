import erosion
import dilation
import cv2
import sys


def closing():
    img = erosion.readImg()
    finalImg =  erosion.erosion(dilation.dilation(img))
    cv2.imwrite(sys.argv[2], finalImg)

if __name__== "__main__":
    closing()
