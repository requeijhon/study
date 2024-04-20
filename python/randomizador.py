import random

inicio_intervalo = 1
fim_intervalo = 100

numero_secreto = random.randint(inicio_intervalo, fim_intervalo)
print(numero_secreto)

print('Tente adivinhar o número secreto entre 1 e 100.')

numero_usuario = (input('Digite um número: '))

try:
    numero_usuario_int = int(numero_usuario)
    if numero_usuario.isdigit():

        while numero_usuario_int != numero_secreto:
    
            if numero_usuario_int > numero_secreto:
                numero_usuario_int = int((input('Errado. O número secreto é menor que o digitado. Tente novamente: '))) 
            else:
               numero_usuario_int = int((input('Errado. O número secreto é maior que o digitado. Tente novamente: ')))

    print('Parabéns, você acertou!')

except ValueError:
     print('Por favor, digite apenas números inteiros.')