import pyautogui

class LoginDominio:
    
    def __init__(self):
        pass

    def userLogin(self, user):
        pyautogui.sleep(20)
        pyautogui.moveTo(x=952, y=498, duration=0.5)
        pyautogui.doubleClick()
        pyautogui.press('delete')
        pyautogui.typewrite(user)

    def passwordLogin(self, password):
        pyautogui.moveTo(x=984, y=534, duration=0.5)
        pyautogui.doubleClick()
        pyautogui.press('delete')
        pyautogui.typewrite(password)
        pyautogui.press('enter')
        pyautogui.sleep(30)