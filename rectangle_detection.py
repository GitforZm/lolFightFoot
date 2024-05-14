import cv2  
import numpy as np  
import pyautogui


      
def detect_and_move_to_rectangle(img):  
    
    lower_color = np.array([0, 220, 40])  
    upper_color = np.array([10, 255, 70])
    
    image = cv2.imread(img)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
    # 将BGR图像转换为HSV图像
    
       
        
 
      
    # 创建掩模  
    mask = cv2.inRange(hsv_image, lower_color, upper_color)  
      
    # 查找轮廓  
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  
      
    # 设定字体、缩放、颜色和厚度  
    font = cv2.FONT_HERSHEY_SIMPLEX  
    font_scale = 0.5  
    font_color = (0, 255, 0)  # BGR color  
    thickness = 1  
      
    # 筛选和绘制矩形  
    for idx, contour in enumerate(contours):  
        # 计算轮廓的边界矩形  
        x, y, w, h = cv2.boundingRect(contour)  
         
        # 计算面积和宽高比  


        
        area = cv2.contourArea(contour)  
        aspect_ratio = float(w) / h  
          
        # 设定筛选条件  
        if (w / h > 0.85 and w / h < 1.03 and w > 10 and area > 100 ):  
            

            cv2.rectangle(image, (x, y), (x+w, y+h), font_color, 2)  
                 
                    # 在矩形旁边打印信息  
            text = f"Area: {area:.2f}, Aspect Ratio: {aspect_ratio:.2f}"  
            text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]  
            text_x = x if x + text_size[0] < image.shape[1] else x - text_size[0]  
            text_y = y - 5 if y - 5 > 0 else y + h + 10  
            cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness)
             #绘制矩形中心并移动鼠标  
            center_x = x + w // 2  
            center_y = y + h // 2
             #定义偏移量（例如，向右移动20个像素，向下移动10个像素）  
            offset_x = 50  
            offset_y = 100
            pyautogui.moveTo(center_x + offset_x, center_y + offset_y, duration=0.08)
              
            # duration参数是可选的，表示移动时间（秒）  
      
    # 显示结果  
    cv2.imshow('Image with detected rectangles', image)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  # 确保关闭所有OpenCV窗口  
  
# 调用函数，传入参数  
