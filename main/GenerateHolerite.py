import pyautogui

class GenerateHolerite:

    def __init__(self):
        pass

    def dominioProcess(self, number, month):

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

        pyautogui.doubleClick(1067, 419)
        oneSecond

        pyautogui.doubleClick(653, 294)
        pyautogui.press('delete')
        pyautogui.write(month)
        oneSecond

        pyautogui.doubleClick(800, 294)
        pyautogui.press('delete')
        pyautogui.write(month)
        oneSecond
        
        pyautogui.click(1003, 327)
        oneSecond
        pyautogui.click(653, 364)
        oneSecond

        pyautogui.click(1002, 419)
        oneSecond
        pyautogui.click(686, 438)
        oneSecond

        pyautogui.click(1289, 523)
        oneSecond
        pyautogui.click(1168, 560)
        oneSecond

        pyautogui.doubleClick(580, 829)
        pyautogui.press('delete')
        oneSecond

        pyautogui.doubleClick(580, 859)
        pyautogui.press('delete')
        oneSecond

        pyautogui.hotkey('alt' + 'o')
        thirdySeconds

        pyautogui.hotkey('ctrl' + 'd')
        fiveSeconds

        pyautogui.press('delete')
        oneSecond

        pyautogui.write('\\tsclient\C\DOCUMENTOS ROTINA\\' + number + '-RecibodePagamento-' + month)