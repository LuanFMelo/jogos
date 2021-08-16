import forca
import adivinhacao

def escolha_jogo():
    print("*********************************")
    print("******Escolha o seu jogo !*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo ?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar() #module + function
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar() #module + function
    print("Fim do jogo!")

if(__name__ == "__main__"):
    escolha_jogo()