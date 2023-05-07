import cv2
import numpy as np
import random

img_height = 500
img_width = 500

img = np.zeros((img_height, img_width, 3), np.uint8)

width = 5
length = 20
color = (255, 255, 255)
point = [250, 250]
step = 5
flag = 'd' #representing in which direction the snake is going
inc = 10 #pixels by which length of snake is going to increase

cv2.rectangle(img, (point[0] - int(width/2), point[1]-int(length/2)), (point[0] + int(width/2), point[1] + int(length/2) ), color, -1)
#cv2.rectangle(img, (point[0] - int(length/2), point[1]-int(width/2)), (point[0] + int(length/2), point[1] + int(width/2) ), color, -1)

grid = [50, 450]
cpointx = random.randint(grid[0], grid[1])
cpointy = random.randint(grid[0], grid[1])
size = 40

cv2.rectangle(img, (cpointx-int(size/2), cpointy - int(size/2)), (cpointx + int(size/2), cpointy + int(size/2)), color, -1)

while True:

    if flag == 'd':
        if(point[1] + int(length/2) + step > img_height):

            toppoint = [point[0], int(step/2)]
            tpoint = [point[0], point[1]] #temporary point
            for i in range(int(length/step)):

                cv2.rectangle(img, (toppoint[0] - int(width/2), toppoint[1]-int(step/2)), (toppoint[0] + int(width/2), toppoint[1] + int(step/2) ), color, -1)
                cv2.rectangle(img, (point[0] - int(width/2), tpoint[1]-int(length/2)+int(step*i)), (point[0] + int(width/2), tpoint[1] - int(length/2) + int(step*(i+1))), (0, 0, 0), -1)

                point[1] = point[1] + step
                point[1] = point[1]%img_width

                cv2.imshow("IMG", img)
                cv2.waitKey(20)
                toppoint[1] += step

            point[1] = int(length/2)

        else:
            cv2.rectangle(img, (point[0] - int(width/2), point[1]-int(length/2)), (point[0] + int(width/2), point[1] + int(length/2) ), (0, 0, 0), -1)
            point[1] += step
            cv2.rectangle(img, (point[0] - int(width/2), point[1]-int(length/2)), (point[0] + int(width/2), point[1] + int(length/2) ), color, -1)

        if abs(point[0]-cpointx) < int(size/2) and abs(point[1] + int(length/2) - cpointy) < int(size/2):
            length = length + inc

            cv2.rectangle(img, (cpointx-int(size/2), cpointy - int(size/2)), (cpointx + int(size/2), cpointy + int(size/2)), (0, 0, 0), -1)

            cpointx = random.randint(grid[0], grid[1])
            cpointy = random.randint(grid[0], grid[1])

            cv2.rectangle(img, (cpointx-int(size/2), cpointy - int(size/2)), (cpointx + int(size/2), cpointy + int(size/2)), color, -1)






 
    elif flag == 'r':


        if(point[0] + int(length/2) + step > img_width):

            startpoint = [int(step/2), point[1]]
            tpoint = [point[0], point[1]] #temporary point

            for i in range(int(length/step)):

                cv2.rectangle(img, (startpoint[0] - int(step/2), startpoint[1]-int(width/2)), (startpoint[0] + int(step/2), startpoint[1] + int(width/2) ), color, -1)
                cv2.rectangle(img, (tpoint[0] - int(length/2) + int(step*i), point[1]-int(width/2)), (tpoint[0] - int(length/2) + int(step*(i+1)), point[1] + int(width/2)), (0, 0, 0), -1)

                point[0] = point[0] + step
                point[0] = point[0]%img_width

                cv2.imshow("IMG", img)
                cv2.waitKey(20)
                startpoint[0] += step

            #point[0] = int(length/2)

        else:
            cv2.rectangle(img, (point[0] - int(length/2), point[1]-int(width/2)), (point[0] + int(length/2), point[1] + int(width/2) ), (0, 0, 0), -1)
            point[0] += step
            cv2.rectangle(img, (point[0] - int(length/2), point[1]-int(width/2)), (point[0] + int(length/2), point[1] + int(width/2) ), color, -1)
        
        if abs(point[1]-cpointy) < int(size/2) and abs(point[0] + int(length/2) - cpointx) < int(size/2):
            length = length + inc

            cv2.rectangle(img, (cpointx-int(size/2), cpointy - int(size/2)), (cpointx + int(size/2), cpointy + int(size/2)), (0, 0, 0), -1)

            cpointx = random.randint(grid[0], grid[1])
            cpointy = random.randint(grid[0], grid[1])

            cv2.rectangle(img, (cpointx-int(size/2), cpointy - int(size/2)), (cpointx + int(size/2), cpointy + int(size/2)), color, -1)

            

    cv2.imshow("IMG", img)
    s = cv2.waitKey(20)

    if s == ord('d') and flag == 'd':
        startpoint = [point[0], point[1] + int(length/2)-int(width/2)]
        for i in range(int(length/step)):

            cv2.rectangle(img, (startpoint[0] - int(step/2), startpoint[1]-int(width/2)), (startpoint[0] + int(step/2), startpoint[1] + int(width/2) ), color, -1)
            cv2.rectangle(img, (point[0] - int(width/2), point[1]-int(length/2)+int(step*i)), (point[0] + int(width/2), point[1] - int(length/2)+ int(step*(i+1))), (0, 0, 0), -1)
            cv2.imshow("IMG", img)
            cv2.waitKey(20)
            startpoint[0] += step

        point[0] = point[0] + int(length/2)
        point[1] = point[1] + int(length/2)-int(width/2)

        flag = 'r'

    if s == ord('s') and flag == 'r':
        startpoint = [point[0] + int(length/2)-int(width/2), point[1]]
        for i in range(int(length/step)):

            cv2.rectangle(img, (startpoint[0] - int(width/2), startpoint[1]-int(step/2)), (startpoint[0] + int(width/2), startpoint[1] + int(step/2) ), color, -1)
            cv2.rectangle(img, (point[0] - int(length/2) +int(step*i) , point[1]-int(width/2)), (point[0] - int(length/2)+ int(step*(i+1)), point[1] + int(width/2) ), (0, 0, 0), -1)
            cv2.imshow("IMG", img)
            cv2.waitKey(20)
            startpoint[1] += step

        point[0] = point[0] + int(length/2) -int(width/2)
        point[1] = point[1] + int(length/2)

        flag = 'd'

    if s == ord('q'):
        break


cv2.destroyAllWindows()

