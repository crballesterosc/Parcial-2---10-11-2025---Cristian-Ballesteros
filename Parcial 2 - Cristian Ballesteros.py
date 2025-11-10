print("\n")
print("Autor - Cristian Ballesteros :D")
print("Parcial 2 - Programacion de Computadores")
a = 1


def Problema1():
    list1 = [2, 2, 3, 4, 2]
    lists = sorted(list1)
    listF = []

    print(f"La lista es: {list1}")
    print(f"La lista ordenada es: {lists}")
    for e in lists:
        if lists[e] != lists[e-1]:
            listF.append(e)
    print(f"Los elementos que no estan repetidos son: {listF}")
            
def Problema2():
    list1 = ["Hola","Hola","Hola","Hola"]
    

     
def Problema3():
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [1, 2, 3, 4, 5]

    print(f"La lista #1 es: {list1}")
    print(f"La lista #2 es: {list2}") 

    diferencia = [elemento for elemento in list1 if elemento not in list2]

    print(f"Elementos de la lista1 que no estan en la lista2: {diferencia}")  

def Problema4():
    arr1 = [10, 10, 10, -2, -8]
    print(f"Este es tu array: {arr1}")
    a = 0
    for z in (arr1):
        a += z
    mid = len(arr1)
    print(f"El promedio es: {(a/mid)}")



while(a <= 4):
    a+=1
    print("\n")
    val = int(input("Ingrese el valor del problema que desea revisar: "))
    print("\n")
    print(f"Problema {val}")
  
    if (val == 1):
        Problema1()
    elif (val == 2):
        Problema2()
    elif (val == 3):
        Problema3()
    elif (val == 4):
        Problema4()
    else:
        print("Opcion no valida :(")