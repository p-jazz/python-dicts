# Crear una función que reciba 2 números y retorno al menor

def minor_number(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
print(f"El número menor es {minor_number(5,8)}")
