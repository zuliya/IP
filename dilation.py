# How to use
# 0. Open terminal
# 1. cd to the folder with all the files
# 2. type [<python> <dilation.py> <initial pic name> <outputpic name>]



import sys
import cv2
import numpy as np
import erosion

# Invert the image
def invert (img):
    #height = h    width = w
    h, w = np.shape(img)
    for y in range (0, h):
        for x in range (0,w):
            # to invert image take 255- pixel values
            img[x][y]= 255-img[x][y]
    return img

def dilation(img):
    # invert image
    img = invert(img)
    # erode it
    img = erosion.erosion(img)
    # inver the image back 
    img = invert(img)
    return img
    

def main():
    # use erosion to read the file
    img = erosion.readImg()
    # dilate it 
    img = dilation(img)   
    if sys.argv[0] == "opening.py" or sys.argv[0] == "closing.py":
        return img
    else:
        cv2.imwrite(sys.argv[2],img)

if __name__== "__main__":
    main()




