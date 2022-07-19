#Gerador Mega Sena
from random import randint

x = 0
lista = []

while x <= 5:
    sorteado = randint(1, 60)
    if sorteado not in lista:
        lista.append(sorteado)
    else:
        x = x - 1
    x+=1

lista.sort()
print(f'Gerador mega sena: {str(lista)[1:-1]}')
