import pyautogui

class GenerateHolerite:

    def __init__(self):
        pass

    def dominioProcess(self, number):

        path = r'C:\\DOCUMENTOS ROTINA'
        oneSecond = pyautogui.sleep(1)
        fiveSeconds = pyautogui.sleep(5)
        tenSeconds = pyautogui.sleep(10)
        thirdySeconds = pyautogui.sleep(30)
        fullPath = str(path + '\\' + number + '.pdf')

        print('start ' + number + ' company.')
        tenSeconds

        pyautogui.press('f8')
        oneSecond

        pyautogui.write(number)
        oneSecond

        pyautogui.press('enter')
        tenSeconds

        pyautogui.press('esc')
        pyautogui.press('esc')
        pyautogui.press('esc')
        oneSecond

        pyautogui.click(960, 540)
        oneSecond

        pyautogui.hotkey('alt' + 'r')
        oneSecond
        pyautogui.press('r')
        oneSecond
        pyautogui.press('f')
        fiveSeconds
