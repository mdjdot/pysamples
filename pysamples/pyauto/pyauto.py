#!/usr/bin/env python
"""
https://pyautogui.readthedocs.io/en/latest/quickstart.html
PyAutoGUI works on Windows, macOS, and Linux
- 移动鼠标并单击或键入其他应用程序的窗口。
- 向应用程序发送击键（例如，填写表单）。
- 截屏，并给出图像（例如，按钮或复选框），在屏幕上找到它。
- 找到应用程序的窗口，并移动、调整大小、最大化、最小化或关闭它（目前仅限 Windows）
- 在运行 GUI 自动化脚本时显示用户交互的消息框。
"""

import pyautogui

if __name__ == "__main__":
    print(pyautogui.size())
    # print(pyautogui.getAllTitles())
    pyautogui.screenshot('01.png')

    print(pyautogui.position())
    pyautogui.move(20, 30)
    print(pyautogui.position())

    pyautogui.write('123',interval=3)
    pyautogui.keyDown('shift')
    pyautogui.press('z')

    pyautogui.Window().
