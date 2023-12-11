def calcular_idade():
    while True:

        # Função que captura a data atual.
        from datetime import date
        data_atual = (date.today().year)

        # Recebe os dados do usuário.
        nome = str(input("Qual o seu nome completo? "))
        ano_nasc = int(
            input("Digite seu ano de nascimento (Somente entre 1922 e 2021): "))

        # Aplica a restrição de intervalo de anos.
        if (ano_nasc < 1922 or ano_nasc > 2021):
            print("Data não suportada! Fora do intervalo permitido.")
            continue

        # Calculando a idade.
        idade = data_atual - ano_nasc
        print(f"{nome}, sua idade atual é: {idade} anos!")


# Chamando a função.
calcular_idade()
