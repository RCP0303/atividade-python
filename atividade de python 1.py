
while True:
    idade_dias = int(input("Digite sua idade em dias (ou 0 para sair): "))

    if idade_dias == 0:
        print("programa encerrado")
        break

    anos = idade_dias // 365
    resto = idade_dias % 365
    meses = resto // 30
    dias = resto % 30

    print("Idade aproximada:")
    print("Anos:", anos)
    print("Meses:", meses)
    print("Dias:", dias)
    print("----------------------")
