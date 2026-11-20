import random

numero = random.randint(1, 2000000000)

if numero > 1480000000:
    print(f'O número {numero} é maior que a população da Índia.')
elif numero > 214200000:
    print(f'O número {numero} é maior que a população do Brasil.')
elif numero > 11000000:
    print(f'O número {numero} é maior que a população de Portugal.')
else:
    print(f'O número {numero} é maior que a população de Marte.')