def jogar():
    import random

    print("+++++++++++++++++++++++++++++")
    print("Bem-vindo ao jogo da adivinhação!")
    print("+++++++++++++++++++++++++++++")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Qual o nível de dificuldade? ")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha o nível: "))
    if nivel == 1:
        totaldetentativas = 20
    elif nivel == 2:
        totaldetentativas = 10
    else:
        totaldetentativas = 5

    for rodadas in range(totaldetentativas + 1):
        print("tentativa {} de {}".format(rodadas, totaldetentativas))
        chute = int(input("digite um número entre 1 e 100: "))
        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute

        if chute < 1 or chute > 100:
            print("numero invalido")
            continue

        if acertou:
            print("vc acertou e fez {} pontos".format(pontos))
            break

        else:
            if maior:
                print("x maior que o numero desejado")
            elif menor:
                print("x menor que o numero desejado")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("fim do jogo")


if __name__ == "__main__":
    jogar()
