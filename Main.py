# 동영상 파일 읽기 (video_play.py)
import os
import cv2
import numpy as np
from function import Yellow_filter, White_filter, StraightLine_detection




video_file = os.path.join('dataset', 'challenge_video.mp4') # 동영상 파일 경로

cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    while True:
        ret, img = cap.read()   # 프레임 읽기
        # 관심영역 지정
        x, y, w, h = 0, int(img.shape[0]/2)+50, img.shape[1], img.shape[0]
        width_roi = img[y:y+h, x:x+w]
        height_roi = img[y:y+h, x:x+w]
        cv2.rectangle(img, (x,y), (w-1, h-1), (0,255,0))

        # 관심영역 색 추출하기
        yellow_roi = Yellow_filter(width_roi)
        white_roi = White_filter(width_roi)
        mask = cv2.bitwise_or(yellow_roi, white_roi)

        straight_line = StraightLine_detection(mask)
        mask = cv2.bitwise_or(mask, straight_line)
        if ret:                     
            cv2.imshow(video_file, mask)
            if cv2.waitKey(10)&0xFF == 27: # ESC 입력시 종료
                break
        else:
            break
else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()