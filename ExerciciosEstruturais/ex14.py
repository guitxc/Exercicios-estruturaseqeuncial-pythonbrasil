limite = 50.0
multa_valor = 4.0
peso = float(input('Peso total de peixes em quilos: '))
if peso > limite:
    excesso = peso - limite
    multa = excesso * multa_valor
else:
    excesso = 0
    multa = 0
print('Relatorio da Pesca')
print(f'Quilos totais de peixe:KG{peso}')
print(f'Excesso de peixes:KG{excesso}')
print(f'Multa a pagar:R${multa}')