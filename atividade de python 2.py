
import math

while True:
    print("\n--- verificação de triângulo ---")

    a = int(input("digite o primeiro lado(0 para sair):"))

    if a == 0:
        print("programa encerrado")
        break

    b = int(input("digite o segundo lado: "))
    c = int(input("digite o terceiro lado: "))

    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        semiperimetro = (a + b + c) / 2

        area = math.sqrt(
            semiperimetro
            * (semiperimetro - a)
            * (semiperimetro - b)
            * (semiperimetro - c)
        )

        print("\nOs valores formam um triângulo")
        print("Lados:", a, b, c)
        print("Área:", round(area, 2))

    else:
        print("\nOs valores não formam um triângulo")
        print("valores digitados:", a, b, c)

    print("------------------------------")
