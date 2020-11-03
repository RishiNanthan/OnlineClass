import cv2
import pyautogui as pg
import numpy as np


class VideoCamera(object):
    def __init__(self):
        self.vid = cv2.VideoCapture(0)

    def get_frame(self):
        frame = np.array(pg.screenshot())
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame, (700, 500))
        #_, frame = self.vid.read()
        #frame = cv2.flip(frame,1)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

