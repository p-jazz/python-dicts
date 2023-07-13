# Algunas de las funciones que hemos visto entregan de vuelta su resultado, por ejemplo la funcion input() entrega lo escrito por el usuario y luego lo podemos asignar a una variable.

name = input("Dime tu nombre: ")

print(name)

test = print("Hola mundo")

print(test)

# Las funciones que no rettornan nada o que retornnan el valor especial **None** se les conoce como funciones void(vacío)

# Si queremos que nuestra funcion retorne un valor, lo indicamos con la palabra reservada **return**

def multiply_by_two(number):
    return number * 2

result = multiply_by_two(2)
print(result)