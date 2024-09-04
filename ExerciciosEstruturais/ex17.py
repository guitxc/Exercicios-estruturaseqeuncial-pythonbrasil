import math

area_pintada = float(input('Informe o tamanho da area a ser pintada:'))
cobertura_tinta = 6
preço_lata = 80
preço_galão = 25
litros_lata = 18
litros_galão = 3.6
litros_necessarios = area_pintada / cobertura_tinta * 1.10

apenas_lata = math.ceil(litros_necessarios / litros_lata)
custo_lata = litros_necessarios * preço_lata

apenas_galão = math.ceil(litros_necessarios / litros_galão)
custo_galão = litros_necessarios * preço_galão

latas_mistas = int(litros_necessarios // litros_lata)
resto_litros = litros_necessarios % litros_lata
galoes_mistos = resto_litros / litros_galão
custo_misto = (latas_mistas * preço_lata) + (galoes_mistos * preço_galão)
print("\nCálculo de Tintas")
print(f"Área a ser pintada: {area_pintada:.2f} metros quadrados")
print(f"Quantidade de tinta necessária (com folga de 10%): {litros_necessarios:.2f} litros")

print("\nSituação 1: Apenas latas de 18 litros")
print(f"Quantidade de latas necessárias: {apenas_lata}")
print(f"Preço total: R$ {custo_lata}")

print("\nSituação 2: Apenas galões de 3,6 litros")
print(f"Quantidade de galões necessários: {apenas_galão}")
print(f"Preço total: R$ {custo_galão:.2f}")

print("\nSituação 3: Mistura de latas e galões")
print(f"Quantidade de latas necessárias: {latas_mistas}")
print(f"Quantidade de galões necessários: {galoes_mistos}")
print(f"Preço total: R$ {custo_misto:.2f}")