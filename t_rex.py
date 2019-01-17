#pip install time, Pillow, opencv-python, pyautogui, numpy

import time
from PIL import Image
import cv2 #코드중 OpenCV 함수 호출을 위해 모듈을 임포트 해야함
import numpy as np
import pyautogui as pg
from PIL import ImageGrab
# https://opencv-python.readthedocs.io/en/latest/doc/08.imageProcessing/imageProcessing.html
# Reference : https://github.com/shubham99bisht/Python-plays-Dino 


def jump():
    for x0 in range(160,250,5):
        px = img[60,x0]
        print(px[0:1])
        #default : 247
        #another : 83~n 
        if (px[0]<=180):
            print("jump \n")
            pg.keyDown('space')
            time.sleep(0.05)


x, y, w, h = 111, 488, 248, 85
while True:
    img = ImageGrab.grab()   #이미지 캐치
    #저장을 하지않는 이유 : 3배 느려진다. 게임은 반응속도가 중요
    #PIL, PyautoGUI, MSS 스크린 캡처 속도 비교 : http://kolikim.tistory.com/41
    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    #np.array(img) : 이미지를 배열로 변환한다.
    #img의 RGB로 바꿔줌
    img = img[ y:y+h, x:x+w ]
    #이미지 범위
    #488:573, 111:359
    jump()
