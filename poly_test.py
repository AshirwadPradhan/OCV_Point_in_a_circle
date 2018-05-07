import cv2
import matplotlib.pyplot as plt
import math

def main(circle_x, circle_y, given_point_x, given_point_y, circle_rad):
    data_img = 'data/5.1.12.tiff'

    # read data
    img = cv2.imread(data_img, 1)

    # show the circle in blue
    cv2.circle(img,(circle_x, circle_y), circle_rad, (0,0,255), 2)
    # show given point in green
    cv2.circle(img, (given_point_x, given_point_y), 3, (0,255,0), -1)

    # calculate distance between circle center and the given point
    dist = math.sqrt((circle_x - given_point_x)**2 + (circle_y - given_point_y)**2)

    print(dist)
    # if the distance is less than equal to the radius then point is within the circle
    if abs(dist) <= circle_rad:
        print("Point inside the circle")
    else:
        print("Point outside the circle")

   
    # Plotting the image
    plt.imshow(img, cmap='Greys')
    plt.title('Point test')
    plt.xticks([])
    plt.yticks([])
    plt.show()


if __name__=='__main__':

    # circle center x, y and radius
    circle_x = 185
    circle_y = 128
    circle_rad = 6

    # given point x, y
    given_point_x = 200
    given_point_y = 130
    main(circle_x, circle_y, given_point_x, given_point_y, circle_rad)