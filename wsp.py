import pyautogui as pg
import time
import webbrowser as web
phone_no="+593 98 552 8488"
parsedMessage=" "
web.open('https://web.whatsapp.com/send?phone=+')
time.sleep(8)
for i in range(20):
    
    pg.write('Hi xd')
    pg.press('enter')

    print('Mensaje #'+str(i+1)+' enviado')
    pass
pg.alert('Bomba de mensajes finalizada')