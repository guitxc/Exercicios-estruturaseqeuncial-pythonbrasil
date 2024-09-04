horas_trabalhadas = float(input('Quantas horas voce trabalhou no mês? '))
valor_horas = float(input('Quanto você ganha por hora? '))
salario_bruto = horas_trabalhadas * valor_horas
imposto_de_renda = (11 / 100) * salario_bruto
inss = (8 / 100) * salario_bruto
sindicato = (5 / 100) * salario_bruto
salario_liquido = (((salario_bruto - imposto_de_renda) - inss)- sindicato)
print('-----------------------------------------------')
print(f'Seu salario bruto foi de R${salario_bruto}')
print(f'Pagou de imposto de renda R${imposto_de_renda}')
print(f'Pagou ao INSS R${inss}')
print(f'Pagou ao sindicato R${sindicato}')
print(f'Salario liquido R${salario_liquido}')
print('-----------------------------------------------')