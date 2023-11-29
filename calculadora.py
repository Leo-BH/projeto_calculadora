def calculadora(primeiro_numero, segundo_numero, operacao):
    if operacao == 1:
        return primeiro_numero + segundo_numero
    elif operacao == 2:
        return primeiro_numero - segundo_numero
    elif operacao == 3:
        return primeiro_numero * segundo_numero
    elif operacao == 4:
        return primeiro_numero / segundo_numero
    else:
        return 0


def main():
    print("Calculadora Básica")
    primeiro_numero = int(input("Digite um número inteiro: "))
    segundo_numero = int(input("Digite outro número interio: "))

    print('Operações:')
    print("1 -> Soma")
    print("2 -> Subtração")
    print("3 -> Multiplicação")
    print("4 -> Divisão")

    operacao = int(input("Qual o tipo de operação?(1,2,3 ou 4) "))

    resultado = calculadora(primeiro_numero, segundo_numero, operacao)
    print(f"O Resultado da Operação é: {resultado}")


if __name__ == '__main__':
    main()
