notas = []
contador = 1
while contador < 5:
    notas.append(float(input(f'Digite a {contador}° nota: ')))
    contador += 1
media = sum(notas) / len(notas)
print('Sua media é',media)