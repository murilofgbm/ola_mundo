valor_total = int(input("Digite o valor total: "))
porcentagem_do_desconto = int(input("Digite o valor da porcentagem de desconto: "))
valor_do_desconto = (porcentagem_do_desconto/100)*valor_total
valor_total_com_desconto = valor_total - valor_do_desconto 

print(f"Valor total: R${valor_total}") 
print(f"Porcentagem do desconto: {porcentagem_do_desconto}%") 
print(f"Valor do desconto: R${valor_do_desconto}")
print(f"Valor total com desconto: R${valor_total_com_desconto}") 