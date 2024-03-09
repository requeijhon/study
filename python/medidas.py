try: 
    p = float(input('Digite uma medida em pés: '))

    polegadas = p * 12
    jardas = p * 3
    milhas = jardas / 1760

    print('A medida em polegadas é {}, em jardas é {}, e em milhas é {}'.format(polegadas,jardas,milhas))

except  ValueError:
    print('Por favor, insira um valor válido.')





