
def eh_primo(numero):
    if numero < 2:
        return False

    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False

    return True


while True:
    print("\n===== VERIFICADOR DE NÚMEROS PRIMOS =====")
    print("1 -verificar automaticamente de 1 a 100")
    print("2 -digitar um número para verificar")
    print("0 -sair")

    opcao = input("escolha uma opção: ")

    if opcao == "1":
        print("\n--- números de 1 a 100 ---")

        for numero in range(1, 101):
            if eh_primo(numero):
                print(numero, "é primo")
            else:
                print(numero, "não é primo")

    elif opcao == "2":
        while True:
            numero = int(input(
                "\ndigite um número (0 para voltar ao menu): "
            ))

            if numero == 0:
                break

            if eh_primo(numero):
                print("O número", numero, "é primo!")
            else:
                print("O número", numero, "não é primo!")

    elif opcao == "0":
        print("programa encerrado")
        break

    else:
        print("opção inválida.")
