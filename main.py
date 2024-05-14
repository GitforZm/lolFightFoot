# main_program.py  
import pyautogui  
import rectangle_detection  
import numpy as np   
def run_detection():  
    # 调用rectangle_detection.py中的函数
  
      
    # 截取屏幕左上角100x100像素的区域  
    screenshot = pyautogui.screenshot(region=(0, 0, 100, 100))  
  
# 保存截图到文件  
    screenshot.save('screenshot.png')
    rectangle_detection.detect_and_move_to_rectangle("screenshot.png")  
  
# 主程序入口  
if __name__ == "__main__":  
    run_detection()