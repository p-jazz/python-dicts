# Muchas veces es necesario crear una función que reciba un número variable de parámetros o argumentos.
# Es decir, cuando se invoque, llame o ejecute la función, puede recibir un número de variable de parametros

def super_sum(*args):
    result_num = 0
    result_str = ""

    for arg in args:
        if type(arg) == int:
            result_num += arg
        elif type(arg) == str:
            result_str += arg

    return[result_num, result_str]

print(super_sum("A","B"))
print(super_sum(234,2,234,35,34))
print(super_sum(2))
