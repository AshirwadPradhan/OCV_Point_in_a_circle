import cv2
import matplotlib.pyplot as plt
import math

def main(circle_x, circle_y, test_point_x, test_point_y, circle_rad):
    data_img = 'data/5.1.12.tiff'
    # read data
    img = cv2.imread(data_img, 0)

    # first draw the test point so that subsequently drawing the ROI can mask it
    # show given point in white
    img = cv2.circle(img, (test_point_x, test_point_y), 3, (255,255,255), -1)

    # show the circle in black
    img = cv2.circle(img,(circle_x, circle_y), circle_rad, (0,0,0), -1)
    
    if img[test_point_y, test_point_x] == 0:
        print('Point within ROI')
    else:
        print('Point outside ROI')
   
    # show the image
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__=='__main__':

    # circle center x, y and radius
    circle_x = 185
    circle_y = 128
    circle_rad = 6

    # given point x, y
    given_point_x = 200
    given_point_y = 130
    main(circle_x, circle_y, given_point_x, given_point_y, circle_rad)