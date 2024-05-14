# main_program.py  
import pyautogui  
import rectangle_detection  
import numpy as np   
def run_detection():  
    # 调用rectangle_detection.py中的函数
  
      
   


    rectangle_detection.detect_and_move_to_rectangle("image2.jpg")  

  
# 主程序入口  
if __name__ == "__main__":  
    run_detection()
