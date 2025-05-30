import webbrowser
import time
import keyboard

# 打开指定的网页
url = "https://accounts.google.com/"
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open(url)

# 等待网页加载
time.sleep(5)
def open(url):
    """
    This function opens a given URL in a new tab using the webbrowser module.
    """
    #webbrowser.open_new_tab(url)
    keyboard.write('https://accounts.google.com/')
    keyboard.press_and_release('enter')
    time.sleep(3)

def account_and_password():
    """
    This function uses the keyboard library to simulate typing an email and password into a login form.
    It first types the email, presses 'enter', waits for 2 seconds, then types the password and presses 'enter' again.
    """
    keyboard.write('put your account here')  # 输入电子邮件地址
    keyboard.press_and_release('enter')  # 按下并释放 'enter' 键
    time.sleep(3) 
    keyboard.write('put pour password here')  # 输入密码
    keyboard.press_and_release('enter')  # 按下并释放 'enter' 键

open(url)
account_and_password()