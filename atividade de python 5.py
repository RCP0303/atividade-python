
def inverter_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = []

    for palavra in palavras:
        palavras_invertidas.append(palavra[::-1])

    return " ".join(palavras_invertidas)


while True:
    print("\n===== INVERSOR DE PALAVRAS =====")
    print("digite 'sair' para encerrar o programa.")

    frase = input("digite uma frase: ")

    if frase.lower() == "sair":
        print("programa encerrado")
        break

    resultado = inverter_palavras(frase)

    print("frase original:", frase)
    print("frase invertida:", resultado)
    print("--------------------------------")
