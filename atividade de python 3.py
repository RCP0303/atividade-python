
while True:
    print("\n--- encontrar o menor número ---")

    a = int(input("digite o primeiro número (0 para sair):"))

    if a == 0:
        print("programa encerrado")
        break

    b = int(input("digite o segundo número: "))
    c = int(input("digite o terceiro número: "))

    menor = min(a, b, c)

    print("Os números digitados foram:", a, b, c)
    print("O menor número é:", menor)

    print("------------------------------")
