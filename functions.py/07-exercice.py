# Crear una función que reciba 2 números e imprima cual es el menor

def minor_number(num1,num2):
    if num1 < num2:
        print(f"{num1} es menor que {num2}")
    else:
        print(f"{num2} es menor que {num1}")

minor_number(5,8)
minor_number(6,4)
