import adivinhacao
import forca

def escolhe_jogo():
    print("************************************")
    print("Escolha seu jogo!")
    print("************************************")

    print("(1) Adivinhação e (2) Forca")

    jogo = int(input("Qual jogo quer jogar?"))

    if jogo == 1:
        print("Jogando adivinhação")
        adivinhacao.jogo_adivinhacao()
    elif jogo == 2:
        print("Jogando forca")
        forca.jogo_forca()

if(__name__ == "__main__"):
    escolhe_jogo()