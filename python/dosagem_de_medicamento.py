'''
ATIVIDADE
4) Criar um algoritmo que a partir da idade e peso do paciente calcule a dosagem de determinado medicamento e mostre a receita 
informando quantas gotas do medicamento o paciente deve tomar por dose.
Considere que o medicamento em questão possui 500 mg por ml, e que cada ml corresponde a 20 gotas.
Adultos ou adolescentes desde 12 anos, inclusive, se tiverem peso igual ou acima de 60 quilos devem tomar 1000mg; com peso 
abaixo de 60 quilos devem tomar 875 mg.
Para crianças e adolescentes abaixo de 12 anos a dosagem é calculada pelo peso corpóreo conforme a tabela a seguir:

abaixo de 5 kg - nao pode tomar
5 a 9 kg - 125 mg
9,1 a 16 kg - 250 mg
16,1 a 24 kg - 375 mg
24,1 a 30 kg - 500 mg
acima de 30 kg - 750 mg
'''
print('Saiba a dosagem correta do medicamento de acordo com seu peso e idade!')

peso = float(input('Digite seu peso: '))
idade = int(input('Digite sua idade: '))

if (idade >= 12):
    if (peso >= 60):
        print('Você deve tomar 40 gotas(1000mg)')
    else:
        print('Você deve tomar 35 gotas(875mg)')
else:
    if (peso <= 5):
        print('Você não pode tomar este remédio')
    elif (peso > 5 and peso <= 9 ):
        print('Você deve tomar 5 gotas(125mg)')
    elif (peso > 9 and peso <= 16 ):
        print('Você deve tomar 10 gotas(250mg)')
    elif (peso > 16 and peso <= 24 ):
        print('Você deve tomar 15 gotas(375mg)')
    elif (peso > 24 and peso <= 30 ):
        print('Você deve tomar 20 gotas(500mg)')
    else:
        print('Você deve tomar 30 gotas(750mg)')