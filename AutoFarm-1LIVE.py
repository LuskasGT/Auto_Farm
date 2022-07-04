# horario de live começa a 11.30 algo do tipo
#usando a resolução de 1360 x 768

#Esse eu to fazendo para que 1 live seja executada em 1 tela, só a do 4rielzin

import pyautogui
from datetime import datetime  #meu pc ta com 4seg adiantado no site do horario de brasilia
import time

p = 0
horas = datetime.today().strftime('%H:%M:%S') #pega a hora, minuto e o segundo do SEU pc
horario = '12:00:10'   # aqui seria o horario que vc irá colocar para o programa executar o script
navegador = 'Opera GX'     #aqui é o seu navegador, caso queira o google, apenas coloca no lugar do opera 

while True:
    if horas >= horario:
        horas = datetime.today().strftime('%H:%M:%S')
        pyautogui.press('winleft')  #aperta o botão do Windos do lado esquerdo
        time.sleep (3) # fez o pc dormir por 1 seg 
        pyautogui.write (navegador, interval=0.20)    #Escreve o nome do seu navegador
        pyautogui.press('enter')   #aperta enter para acessar

        time.sleep (4) # fez o pc dormir por 1 seg 
        pyautogui.moveTo(798, 52)  #levando para a barra de pesquisa
        pyautogui.click()     #clicando para conseguir digitar

        pyautogui.write('https://www.twitch.tv/4rielzin')    #link da primeira live
        pyautogui.press('enter')    #apertando o enter
        p +=1
        if p == 1:
            break
    else:
        horas = datetime.today().strftime('%H:%M:%S')  # vai fazer a verificação, se chegou no horario ou não
        time.sleep(2400) #ele deixa o pc descançando, assim não puxa tanto o sistema


        