nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
indice = len(nome) - 1

if (not nome) or (not idade):
    print('Desculpe, você deixou campos vazios.') 
else:
    print('Seu nome é:', nome)
    print('Seu nome invertido é:', nome[ : :-1])
    print('Seu nome tem', len(nome), 'letras.')
    print('A primeira letra do seu nome é:', nome[:1])
    print('A última letra do seu nome é:', nome[indice:])

    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')

