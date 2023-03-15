valor_total = int(input("Digite o valor total: "))
valor_do_desconto = (10/100)*valor_total
valor_total_com_desconto = valor_total - valor_do_desconto 

print(f"Valor total: R${valor_total}") 
print(f"Porcentagem do desconto: 10%") 
print(f"Valor do desconto: R${valor_do_desconto}")
print(f"Valor total com desconto: R${valor_total_com_desconto}") 