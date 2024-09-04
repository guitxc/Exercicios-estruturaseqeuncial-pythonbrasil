altura = float(input('Coloque sua altura: '))
sexo = input("Qual o seu sexo (M para masculino e F para feminino): ")
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None
print('Seu peso ideal é', peso_ideal)

