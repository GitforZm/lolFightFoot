import cv2  
import dxcam  # 假设这是一个有效的库  
import numpy as np  
import pyautogui  
import mouse  
import threading  
from pynput.mouse import Listener, Button  # 确保导入了Listener和Button  
from PIL import Image
import rectangle_detection  
import numpy as np
from io import BytesIO   
pyautogui.PAUSE = 0   
CHAMPION_HIGHT_OFFSET, CHAMPION_WIDTH_OFFSET = 198, 130  
ENEMY_COLOR_OFFSET_X, ENEMY_COLOR_OFFSET_Y = 5, 15  
camera = None  
is_bug_on = False  
  
def is_enemy_color(color):  
    B, G, R = color  
    # 调整这些条件以适应您的需求  
    if B > R or G > R:  
        return False  
    if G > 30 or B > 30:  
        return False  
    return R > 50 and R < 70  
  
def start():  
    global is_bug_on  
    if is_bug_on:  
            capture()  
    else:  
        return 


  
def capture():  
    print('capture...')  
    
    #camera.start()  
    lower_dark_red = np.array([0, 50, 50])  
    upper_dark_red = np.array([10, 255, 150])  
      

    rectangle_detection.detect_and_move_to_rectangle(lower_dark_red, upper_dark_red, '', '')  

    #camera.stop()
    del camera    
def on_click(x, y, button, pressed):  
    global is_bug_on  
    if pressed and button == Button.x1:  # 确保从pynput.mouse导入Button  
        if is_bug_on:  
            is_bug_on = False  
            print("Stopped...")  
        else:  
            is_bug_on = True  
            print('starting...')  
            threading.Thread(target=start).start()  # 启动新线程来执行start函数 
with Listener(on_click=on_click) as listener:  
    listener.join()  # 这会阻塞主线程，直到Listener停止  