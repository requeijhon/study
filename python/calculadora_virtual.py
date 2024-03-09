print('Olá, bem vindo à calculadora virtual')
entrada = input('Deseja sair(s/n)?\n ')

while entrada == 'n':
    numero_um = input('Escreva o primeiro número inteiro: ')
    numero_dois = input('Escreva o segundo número inteiro: ')

    operador = input('Escreva o operador(+-/*) ')
    operador_valido_um = '+' 
    operador_valido_dois = '-' 
    operador_valido_tres = '/' 
    operador_valido_quatro = '*' 

    try:
        numero_um_float = int(numero_um)
        numero_dois_float = int(numero_dois)

        if numero_um.isdigit() and numero_dois.isdigit() and ((operador == operador_valido_um) or (operador == operador_valido_dois) or (operador == operador_valido_tres) or (operador == operador_valido_quatro)):
        
            if operador == '+':
                print('O resultado da operação é:', numero_um_float + numero_dois_float)
            elif operador == '-':
                print('O resultado da operação é:', numero_um_float - numero_dois_float)
            elif operador == '/':
                print('O resultado da operação é:', numero_um_float / numero_dois_float)
            else:
                print('O resultado da operação é:', numero_um_float * numero_dois_float)

        else:
            print('Por favor, insira um operador válido.')

    except ValueError:
        print('Por favor, digite números inteiros válidos!')
    
    entrada = input('Deseja sair(s/n)?\n ')





