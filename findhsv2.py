
import cv2
import numpy as np

# img是你的BGR图像
img = cv2.imread('1.png')

# 将BGR图像转换为HSV图像
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 获取H, S, V的最小值和最大值
min_h, max_h = np.min(hsv_img[:,:,0]), np.max(hsv_img[:,:,0])
min_s, max_s = np.min(hsv_img[:,:,1]), np.max(hsv_img[:,:,1])
min_v, max_v = np.min(hsv_img[:,:,2]), np.max(hsv_img[:,:,2])

print(min_h, max_h)
print(min_s, max_s)
print(min_v, max_v)
