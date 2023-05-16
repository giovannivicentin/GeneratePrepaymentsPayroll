import pyautogui

class GenerateHolerite:
    
    def __init__(self):
        pass

    def userLogin(self, user):
        pyautogui.moveTo(x=952, y=498, duration=0.5)
        pyautogui.doubleClick()
        pyautogui.press('delete')
        pyautogui.typewrite(user)

    def passwordLogin(self, password):
        self.click_image('dominio\\pyautogui-images\\password.png')
        pyautogui.moveTo(x=984, y=534, duration=0.5)
        pyautogui.doubleClick()
        pyautogui.press('delete')
        pyautogui.typewrite(password)
        pyautogui.press('enter')
        pyautogui.sleep(30)