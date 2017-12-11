# How to use
# 0. Open terminal
# 1. cd to the folder with all the files
# 2. type [<python> <erosion.py> <initial pic name> <outputpic name>]

import sys
import cv2
import numpy as np

#read
def readImg():
    img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    return img


def erosion(img):
    copyImg = img.copy()
    #height = h    width = w
    h, w = np.shape(img)
    
    # Loop over all pixels 
    for y in range (0, h):
        for x in range (0,w):
            region5_5 = []
            # region 5X5
            for regionY in range(y-2,y+3):
                for regionX in range (x-2,x+3):
                    #ignore out of boundaries values
                    if regionY<0 or regionY>h-1 or regionX<0 or regionX>w-1:
                        continue
                    region5_5.append(img[regionX, regionY])
            #takes minimum value & applies to the middle element in the region
            copyImg[x][y] = min(region5_5)
    return copyImg

def main():
    # use erosion to read the file
    img = readImg()
    # erode it
    imgE = erosion(img)
    if sys.argv[0] == "opening.py" or sys.argv[0] == "closing.py":
        return imgE
    else:
        cv2.imwrite(sys.argv[2],imgE)

if __name__== "__main__":
    main()




