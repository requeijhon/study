faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
estados = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo', 'Outros estados']

total = sum(faturamento)

for i in range(5):
    percentual = (faturamento[i]/total)*100
    print (f'O faturamento de {estados[i]} foi de: {percentual:.2f}%')
