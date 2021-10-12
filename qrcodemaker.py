# Bibliotecas Usadas:
from os import close
import pyqrcode as pqr
import io
import png
from time import sleep
import os
import sys

#Função principal do programa.
def papai():

    while True:

        try:
            os.makedirs("./Qrcodes")

        except:
            pass
# Parte onde você digita o conteúdo do seu QRCODE (Links, Frases, Numero.)
        urlpick = input("Digite o conteúdo ou url do seu QRCODE:  ")
# Aqui ele processa o que foi digitado acima e cria seu QRCODE.
        url = pqr.create(urlpick)
# Aqui nessa váriavel ele armazena o nome que você deseja colocar no seu arquivo PNG (QRCODE)
        nomepick = input(
            "Digite o nome para seu arquivo QRCODE:  ")
# Daqui pra baixo é todo o processo para ele salvar seu arquivo na pasta certinha!
        with open(f'./Qrcodes/{nomepick}.png', 'w') as fstream:
            url.png(f'./Qrcodes/{nomepick}.png', scale=5)
        buffer = io.BytesIO()
        url.png(buffer)
        print("Seu QRCode foi gerado!")
        print("-------------------------------------------------------------------------------")
        sleep(2)
        mamae()

# Definindo a função para o programa.
def mamae():

    while True:
# Aqui usamos a escolha do usuário para fechar o programa, retornar ao uso do programa, ou se o usuário usar uma opção que não condiz, retornar a escolha.
        choice = input(
            "Digite a opção correta:\n1 = Fazer Outro QRCode\n2 = Fechar o programa\n-->: ")

# Opção 1 que retorna o usuário para fazer um novo qrcode.
        if choice == '1':
            sleep(2)
            os.system("cls")
            return papai()

# Opção 2 fecha o programa.
        elif choice == '2':
            print('-------------------------------------------------------------------------------')
            print('Good Bye! =D')
            sleep(2)
            return fechar()
        
# Opção 3 da qualquer outra coisa digitada que não seja 1 ou 2 como errada e retorna para a seleção!
        else:
            print("Opção errada!")
            sleep(1)
            os.system("cls")
            return mamae()

#Feita uma implementação corrigir o bug do script não fechar quando se escolhe a opção (2)
def fechar():
    sys.exit()

# Sem isso o programa não roda, rsrsr
papai()
mamae()
