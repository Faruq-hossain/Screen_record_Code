import cv2
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics
import time


# GetSystemMetrics atar maddhome full screen korarjonno
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
# ata jate 1 video ses hober por onno video jate open na hoi tar jonno
# atate time note kore  fatch korbe hour min sec  proti time alada hbe proti ta alada hbe and pore pass korci capture _video te file name ta
# ========file name=======
file_name = f"video/Video_{str(time.strftime('%d-%m-%Y %H-%M-%S'))}.mp4"
# video save korar jonno
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# fourcc codeter,and 20.0 FPS
capture_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
#webcam = cv2.VideoCapture(1)
# screen capture korar jonno
while True:
    screen_img = ImageGrab.grab(bbox=(0, 0, width, height))
    array_img = np.array(screen_img)  # array k call
    color_img = cv2.cvtColor(array_img, cv2.COLOR_BGR2RGB)  # color dewar jonno
    #_, frame = webcam.read()
    # Video folder e store korar jonno
    capture_video.write(color_img)
    # image show korar jonno name and array_img pass
    cv2.imshow('Screen Recorder By Faruq', color_img)
    #cv2.imshow('webcam', frame)
    if cv2.waitKey(1) == ord('x'):  # video exit korar jonno ord er maddhome
        break
# ato tuky korsr akhon video k convert kore save korbo new folder banabo
