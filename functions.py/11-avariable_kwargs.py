# Al igual que con * podemos pasar un numero variable de argumentos, con ** podemos pasar un numero variable de keyword arguments

def print_dic(**kwargs):
    print(kwargs)

print_dic(name = "Jaz", age = 24)

def super_sum(*args,**kwargs):
    print(args) 
    print(kwargs) 

super_func(1,2,3,4,12, name = "Jaz", age = 24)

super_func()
