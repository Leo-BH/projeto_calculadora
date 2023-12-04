# Calculadora com Loop Infinito
def calculadora_interativa():
    while True:
        # Menu de Operações
        print("Operações:")
        print("1 -> Soma")
        print("2 -> Subtração")
        print("3 -> Multiplicação")
        print("4 -> Divisão")
        print("0 -> Sair")

        # O usuário escolhe o tipo de operação e os valores.
        operacao = int(input("Qual o tipo de operação?(1,2,3 ou 4) "))

        # Verifica a escolha do usuário. (Se a o usuário digitar '0', o progama sai do Loop e exibe uma mensagem)
        if operacao == 0:
            print("Saindo da calculadora...")
            break
        # Execução da Operação.
        elif operacao in range(1, 5):
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))

        if operacao == 1:
            resultado = n1 + n2
            print(f"O Resultado de {n1} + {n2} é igual a: {resultado}")
        elif operacao == 2:
            resultado = n1 - n2
            print(f"O resultado de {n1} + {n2} é igual a: {resultado}")
        elif operacao == 3:
            resultado = n1 * n2
            print(f"O resultado de {n1} * {n2} é igual a: {resultado}")
        elif operacao == 4:
            if n1 and n2 != 0:
                resultado = n1 / n2
                print(f"O resultado de {n1} / {n2} é igual a: {resultado}")
            else:
                print("Não é possível realizar divisão por '0'.")
        else:
            print(" Operação inválida! Tente outra vez.")


calculadora_interativa()
