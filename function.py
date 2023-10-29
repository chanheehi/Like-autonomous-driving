import numpy as np
import cv2
import matplotlib.pyplot as plt

# 노란 차선 필터링
def Yellow_filter(image):
    hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    lower = np.array([20, 150, 20])
    upper = np.array([255, 255, 255])

    yellow_lower = np.array([0, 85, 81])
    yellow_upper = np.array([190, 255, 255])

    yellow_mask = cv2.inRange(hls, yellow_lower, yellow_upper)
    white_mask = cv2.inRange(hls, lower, upper)
    mask = cv2.bitwise_or(yellow_mask, white_mask)
    masked = cv2.bitwise_and(image, image, mask = mask)

    return masked

# 하얀 차선 필터링
def White_filter(image):
    blue_threshold = 200
    green_threshold = 200
    red_threshold = 200
    bgr_threshold = [blue_threshold, green_threshold, red_threshold]

    # BGR 제한 값보다 작으면 검은색으로
    thresholds = (image[:,:,0] < bgr_threshold[0])
    (image[:,:,1] < bgr_threshold[1])
    (image[:,:,2] < bgr_threshold[2])
    image[thresholds] = [0,0,0]

    return image

# 직선 라인 검출
def StraightLine_detection(image):
    edges = cv2.Canny(image,50,200,apertureSize = 3)
    gray = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)

    gray = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
    minLineLength = 100
    maxLineGap = 0

    lines = cv2.HoughLinesP(edges,1,np.pi/180,70,minLineLength,maxLineGap)
    for i in range(len(lines)):
        for x1,y1,x2,y2 in lines[i]:
            cv2.line(image,(x1,y1),(x2,y2),(0,0,255),3)
    return image