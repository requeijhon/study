numero = int(input("Informe um número: "))

a, b = 0, 1

pertence = False

while a <= numero:
    if a == numero:
        pertence = True
        break
    a, b = b, a + b

if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")


