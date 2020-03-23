#!/usr/bin/env python3
"""
Python-UIAutomation-for-Windows
Python 3 wrapper of Microsoft UIAutomation. Support UIAutomation for MFC, WindowsForm, WPF, Modern UI(Metro UI), Qt, IE, Firefox, Chrome ...
https://github.com/yinkaisheng/Python-UIAutomation-for-Windows
automation.py -h
  automation.py -t 0-n，打印当前活动窗口的控件，显示全名
automation.py -r -d 1-t 0，打印桌面（控件树的根）和它的子级（顶级窗口）
"""
import subprocess
import time
import uiautomation as auto


text = """
The uiautomation module
This module is for UIAutomation on Windows(Windows XP with SP3, Windows Vista and Windows 7/8/8.1/10).
It supports UIAutomation for the applications which implmented IUIAutomation, such as MFC, Windows Form, WPF, Modern UI(Metro UI), Qt and Firefox.

Run 'automation.py -h' for help.

uiautomation is shared under the Apache Licene 2.0.
This means that the code can be freely copied and distributed, and costs nothing to use.

代码原理介绍: http://www.cnblogs.com/Yinkaisheng/p/3444132.html
"""

def demo():
    consoleWindow = auto.GetConsoleWindow()
    consoleWindow.SetActive()
    auto.Logger.ColorfullyWriteLine(
        '\nI will open <Color=Green>Notepad</Color> and <Color=Yellow>automate</Color> it. Please wait for a while.')
    time.sleep(2)

    auto.ShowDesktop()

    # 打开notepad
    subprocess.Popen('notepad')

    # 查找notepad， 如果name有中文，python2中要使用Unicode
    notepad = auto.WindowControl(
        searchDepth=1, ClassName='Notepad', RegexName='.* - 记事本')
    # 可以判断window是否存在，如果不判断，找不到window的话会抛出异常
    # if window.Exists(maxSearchSeconds = 3):
    if auto.WaitForExist(notepad, 3):
        auto.Logger.WriteLine("Notepad exists now")
    else:
        auto.Logger.WriteLine(
            "Notepad does not exist after 3 seconds", auto.ConsoleColor.Yellow)

    screenWidth, screenHeight = auto.GetScreenSize()
    notepad.MoveWindow(screenWidth // 4, screenHeight // 4,
                       screenWidth // 2, screenHeight // 2)
    notepad.SetActive()

    # 查找edit
    # or edit = window.EditControl()
    edit = auto.EditControl(searchFromControl=notepad)
    edit.Click(waitTime=0)

    # python2中要使用Unicode, 模拟按键
    edit.GetValuePattern().SetValue('hi你好')
    edit.SendKeys('{Ctrl}{End}{Enter}下面开始演示{! 4}{ENTER}', 0.2, 0)
    edit.SendKeys(text)
    edit.SendKeys('{Enter 3}0123456789{Enter}', waitTime=0)
    edit.SendKeys('ABCDEFGHIJKLMNOPQRSTUVWXYZ{ENTER}', waitTime=0)
    edit.SendKeys('abcdefghijklmnopqrstuvwxyz{ENTER}', waitTime=0)
    edit.SendKeys('`~!@#$%^&*()-_=+{ENTER}', waitTime=0)
    edit.SendKeys('[]{{}{}}\\|;:\'\",<.>/?{ENTER}', waitTime=0)
    edit.SendKeys(
        '™®①②③④⑤⑥⑦⑧⑨⑩§№☆★○●◎◇◆□℃‰€■△▲※→←↑↓〓¤°＃＆＠＼＾＿―♂♀{ENTER}{CTRL}a')
    notepad.CaptureToImage('Notepad.png')
    edit.SendKeys(
        'Image Notepad.png was captured, you will see it later.', 0.05)
    # 查找菜单
    notepad.MenuItemControl(Name='格式(O)').Click()
    notepad.MenuItemControl(Name='字体(F)...').Click()
    windowFont = notepad.WindowControl(Name='字体')
    listItem = windowFont.ListControl(
        searchDepth=2, AutomationId='1000').ListItemControl(Name='微软雅黑')
    if listItem.Exists(2):
        listItem.GetScrollItemPattern().ScrollIntoView()
        listItem.Click()
    windowFont.ComboBoxControl(AutomationId='1140').Select('中文 GB2312')
    windowFont.ButtonControl(Name='确定').Click()
    notepad.GetWindowPattern().Close()
    if auto.WaitForDisappear(notepad, 3):
        auto.Logger.WriteLine("Notepad closed")
    else:
        auto.Logger.WriteLine(
            "Notepad still exists after 3 seconds", auto.ConsoleColor.Yellow)
    # buttonNotSave = ButtonControl(searchFromControl = window, SubName = '不保存')
    # buttonNotSave.Click()
    # or send alt+n to not save and quit
    # auto.SendKeys('{Alt}n')
    # 使用另一种查找方法
    buttonNotSave = notepad.ButtonControl(
        Compare=lambda control, depth: '不保存' in control.Name or '否' in control.Name)
    buttonNotSave.Click()
    subprocess.Popen('Notepad.png', shell=True)
    time.sleep(2)
    consoleWindow.SetActive()
    auto.Logger.WriteLine('script exits', auto.ConsoleColor.Cyan)
    time.sleep(2)


if __name__ == "__main__":
  app = subprocess.Popen('notepad.exe')
  # notepad = auto.WindowControl(ClassName='Notepad')
  notepad = auto.WindowControl(Name='无标题 - 记事本')
  
  notepad.SetActive()
  # notepad.Maximize()
  time.sleep(3)

  menubar = notepad.WindowControl(Automationid='MenuBar')
  menubar.GetChildren()[0].Click()
  time.sleep(3)
  notepad.CaptureToImage('2.png')
  app.kill()