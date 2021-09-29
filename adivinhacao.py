import random


def jogo_adivinhacao():

    print("************************************")
    print("Bem vindo!")
    print("************************************")

    num_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil, (2) Médio e (3) Difícil")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}")
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Digite apenas números entre 1 e 100")
            continue  # continua o laço sem parar

        correto = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto

        if correto:
            print(f"Acertou mizeravi e fez {pontos} pontos")
            break  # para parar o laço
        else:
            if maior:
                print("Eroooooou! Chute maior que o número secreto")
            elif menor:
                print("Eroooooou! Chute menor que o número secreto")
            pontos_perdidos = abs(num_secreto - chute)
            pontos = pontos - pontos_perdidos

    print(f"Fim do jogo! O número secreto era {num_secreto}")


if __name__ == "__main__":
    jogo_adivinhacao()
