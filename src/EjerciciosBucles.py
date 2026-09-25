import random
#Ejercicio 1
listEnteros = []
listEnteros2 = []
contador = 0
numAux = 0
numAux2 = 0

for i in range(15):
    numAux += 1
    listEnteros.append(numAux)

print(listEnteros)

while (contador<20):
    numAux2 += 1
    listEnteros2.append(numAux2)
    contador +=1

print (listEnteros2)

#Ejercicio 2
listaRandom = []
numeroRandom = 0

for i in range(15):
    numeroRandom = random.randint(0,100)
    listaRandom.append(numeroRandom)

print(listaRandom)

listaRandom2 = []
numeroRandom2 = 0
contadorRandom = 0;
while(contadorRandom<13):
    numeroRandom2 = random.uniform(3,5)
    numeroRandom2 = round(numeroRandom2,2)
    listaRandom2.append(numeroRandom2)
    contadorRandom += 1

print(listaRandom2)

listaRandom3 = []
valorRandom = ""
for i in range(4):
    valorRandom = random.choice(['Izquierda', 'Derecha', 'Arriba', 'Abajo'])
    listaRandom3.append(valorRandom)

print(listaRandom3)