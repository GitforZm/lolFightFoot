import pyautogui  
import rectangle_detection  
from pynput.keyboard import Key, Listener  
from threading import Thread  
  
def rmyfun():  
    # 截取屏幕左上角100x100像素的区域  
    screenshot = pyautogui.screenshot()  
    # 保存截图到文件  
    screenshot.save('screenshot.png')  
    # 调用rectangle_detection.py中的函数，并使用正确的文件名  
    rectangle_detection.detect_and_move_to_rectangle("screenshot.png")  
    print("空格键被按下，执行了rmyfun函数")  
  
def on_press(key):  
    if key == Key.space:  # 如果按下的键是空格键  
        rmyfun()  
  
def listen_for_space_key():  
    with Listener(on_press=on_press) as listener:  
        listener.join()  # 监听将持续进行，直到程序被中断  
  
# 创建一个线程（非守护线程）来监听空格键  
keyboard_listener_thread = Thread(target=listen_for_space_key)  
keyboard_listener_thread.start()  
  
# 主线程可以继续执行其他任务  
print("请按下空格键以执行检测...")  
  
# 示例：主线程可以执行一些其他任务，比如等待用户输入  
try:  
    input("按任意键退出程序...")  
except KeyboardInterrupt:  
    pass  # 如果用户按下Ctrl+C，则退出程序  
  
# 当主线程结束时，由于keyboard_listener_thread不是守护线程，  
# 它将继续运行，直到程序被外部中断（如Ctrl+C）或显式停止