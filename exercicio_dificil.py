nome = input()
if nome == "Pedro" or nome == "Maria" or nome == "Paulo" or nome == "Ana":
    print("Você não é apto para continuar este cadastro.")
else:
    idade = int(input())
    if idade < 18 or idade > 30:
        print("Você não é apto para continuar este cadastro.")
    else:
        endereco = input()
        if "rua" in endereco:
            print("Cadastro completo.")
        while "rua" not in endereco:
            endereco = input()
            if "rua" in endereco:
                print("Cadastro completo.")
            