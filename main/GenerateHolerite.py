import pyautogui
import time
class GenerateHolerite:

    def __init__(self):
        pass

    def dominioProcess(self, number, month):

        path = r'C:\\DOCUMENTOS ROTINA'
        fullPath = str(path + '\\' + number + '.pdf')

        print('start ' + number + ' company.')
        time.sleep(10)

        pyautogui.doubleClick(960, 540)
        time.sleep(1)
        
        pyautogui.press('f8')
        time.sleep(1)

        pyautogui.write(number)
        time.sleep(1)

        pyautogui.press('enter')
        time.sleep(10)

        pyautogui.press('esc')
        pyautogui.press('esc')
        pyautogui.press('esc')
        time.sleep(1)

        pyautogui.click(960, 540)
        time.sleep(5)

        pyautogui.click(483, 63)
        time.sleep(1)
        pyautogui.press('r')
        time.sleep(1)
        pyautogui.press('f')
        time.sleep(5)

        pyautogui.doubleClick(1067, 419)
        time.sleep(1)

        pyautogui.doubleClick(653, 294)
        pyautogui.press('delete')
        pyautogui.write(month)
        time.sleep(1)

        pyautogui.doubleClick(800, 294)
        pyautogui.press('delete')
        pyautogui.write(month)
        time.sleep(1)
        
        pyautogui.click(1003, 327)
        time.sleep(1)
        pyautogui.click(653, 364)
        time.sleep(1)

        pyautogui.click(1002, 419)
        time.sleep(1)
        pyautogui.click(686, 438)
        time.sleep(1)

        pyautogui.click(1289, 523)
        time.sleep(1)
        pyautogui.click(1168, 560)
        time.sleep(1)

        pyautogui.doubleClick(580, 829)
        pyautogui.press('delete')
        time.sleep(1)

        pyautogui.doubleClick(580, 859)
        pyautogui.press('delete')
        time.sleep(1)

        pyautogui.click(1420, 275)
        time.sleep(30)

        pyautogui.click(40, 435)
        time.sleep(5)

        pyautogui.press('delete')
        time.sleep(1)

        pyautogui.write('\\' + '\\tsclient\\C\\DOCUMENTOS ROTINA\\' + number + '-RecibodePagamento-' + month)
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.click(1023, 609)
        time.sleep(25)

        pyautogui.click(960, 540)
        pyautogui.click(1886, 14)
        time.sleep(10)

        pyautogui.click(960, 540)
        pyautogui.press('esc')
        pyautogui.press('esc')
        pyautogui.press('esc')
        time.sleep(1)
        pyautogui.press('esc')
