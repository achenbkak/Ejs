print("Hello world")
print("mme gusta la caca")
message = "a"
message2 = "b"
full_message = f"{message} {message2}"
x, y, z = 0,1,2
print(x,y,z)
num = 1_234_56
print("\n",num)

def fibo():
    lista = [0,1]
    for i in range(10):
        suma = lista[len(lista)-2] + lista[len(lista)-1]
        lista.append(suma)

    print(lista)
    
fibo()
