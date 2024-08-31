#Não encontrei o arquivo contendo dados do faturamento mensal, então trabalhei com valores criados pelo Chat GPT.
faturamento_diario = [
    1200.50, 1350.75, 1400.00, 1300.25, 1250.00, 1450.10, 1500.80,
    1600.90, 1550.00, 1700.25, 1800.40, 1750.30, 1650.20, 1600.50,
    1550.60, 1500.75, 1400.80, 1450.90, 1550.00, 1600.10
]
faturamento_maior = []

media = sum(faturamento_diario) / len(faturamento_diario)

for i in range(20):
    if faturamento_diario[i] > media:
        faturamento_maior.append(faturamento_diario[i])

print('A média do faturamento mensal foi de:', media)        
print ('Os dias em que o faturamento foram maiores que a média mensal foram:', faturamento_maior)
print('O menor faturamento do mês foi:', min(faturamento_diario))
print('O maior faturamento do mês foi:', max(faturamento_diario))
