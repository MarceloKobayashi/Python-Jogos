import random


def jogar():
    apresentacao()  # 1
    palavra_secreta = secret_word()  # 2

    letras_acertadas = escreve_letras_acertadas(palavra_secreta)  # 3

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = pedir_chute()  # 4

        if chute in palavra_secreta:
            escreve_chute_certo(chute, palavra_secreta, letras_acertadas)  # 5
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        vencedor()  # 6
    elif enforcou:
        perdedor(palavra_secreta)  # 7


def apresentacao():
    print("+++++++++++++++++++++++++++++")
    print("Bem-vindo ao jogo da forca!")
    print("+++++++++++++++++++++++++++++")


def secret_word():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def escreve_letras_acertadas(palavra):
    return ["_" for _ in palavra]


def pedir_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute


def escreve_chute_certo(chute, palavra_secreta, letras_acertadas):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[posicao] = letra
        posicao += 1
    return letras_acertadas


def vencedor():
    print("Você ganhou!")


def perdedor(palavra_secreta):
    print("Você perdeu!")
    print("A palavra era {}".format(palavra_secreta))


if __name__ == "__main__":
    jogar()
