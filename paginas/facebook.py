
import pyautogui
import time
access_token = "EAANDGZBr5QJsBADG8rjk8B9eHCmBfEsc2vrhpzOfZC8nbIVmmH4cKiq8Hi1voy1pZBZCSw4y47BZBzz7TERzt4WvHarm8G1fZBeRyxBrpJ0QEZB6myijhVOewNbYFHJmE2bGFZBHGp2VnbReSh927Bg4YX6A62oKGGK8IQybZBxVHqvwYC2g1T2ZB2dVzfJh4KwcDNgdlcurrNZAmeQoudGFoKe0Vaf7Ft4uyOYXhbmTpTLCisIzxkyhSRY" 
#Polivan123!Facebook
groups = ["373393147649327"]#"422967354533636","421339211240260","1611229439156131","476167535873687","132782420200421","931638116927492","189591658045987","1523194277945996","968365383185165","507779042949896","1712321885650135","516690695076753","251906828330365"]

time.sleep(5)

pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

for i in range(len(groups)):
    link = 'https://facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')

    print("Waiting for 5 seconds\n")
    time.sleep(5)

    pyautogui.typewrite('p')
    time.sleep(2)
    print("Writing post\n")
    pyautogui.typewrite("Hello there, it's a testing post from messy programmers")
    time.sleep(4)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')

    time.sleep(3)

    pyautogui.write(['f6'])
    time.sleep(1)
