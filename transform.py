import numpy as np
import cv2

def reorder(points):
        # we want to save the previous points shape

        # newPoints = np.zeros_like(points)          
        points = points.reshape((4 , 2))
        add = points.sum(axis = 1)
        
        # top left hand corner has the least
        # summation of height and width values
        tl = points[np.argmin(add)]
        
        # bottum right hand corner has
        # most summation of height and width values   
        br = points[np.argmax(add)]       
        diff = np.diff(points , axis = 1)
        
        # top right hand corner has least diff between height and width,
        # in other words top right hand corner has more larger width than height
        tr = points[np.argmin(diff)]

        # buttom hand corner has most diff between height and width, in other words
        # buttom left hand corner has more larger height than width
        bl = points[np.argmax(diff)]      
        return np.array([tl, tr, br, bl], dtype = "float32")

def four_point_transform(image, pts):
        # obtain a consistent order of the points and unpack them
        # individually
        rect = reorder(pts)
        (tl, tr, br, bl) = rect

        # compute the width of the new image, which will be the
        # maximum distance between bottom-right and bottom-left
        # x-coordiates or the top-right and top-left x-coordinates
        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))

        # compute the height of the new image, which will be the
        # maximum distance between the top-right and bottom-right
        # y-coordinates or the top-left and bottom-left y-coordinates
        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        maxHeight = max(int(heightA), int(heightB))

        # now that we have the dimensions of the new image, construct
        # the set of destination points to obtain a "birds eye view",
        # (i.e. top-down view) of the image, again specifying points
        # in the top-left, top-right, bottom-right, and bottom-left
        # order
        dst = np.array([
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]], dtype = "float32")

        # compute the perspective transform matrix and then apply it
        M = cv2.getPerspectiveTransform(rect, dst)
        warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

        # return the warped image
        return warped