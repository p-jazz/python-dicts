# Crear un diccionario vacío
dic = {}

# Crear un diccioanrios conn sus respectivas llaves y valores
dic = {'name':'john', 'age':25, 'city':'London'}

# Accediendo al valor a través de la llave
print(dic['name'])
print(dic['age'])
print(dic['city'])

# Modificar un valor existente
dic['age'] = 30 # Se accede también mediante la llave
print('-------')
print(dic['age']) # Imprime 30, el nuevo valor

# Agregar un nuevo par llave-valor 
dic['hero'] = 'Batman'
print('-------')
print(dic)

# Eliminar un par llave-valor mediante la llave
del dic['age']
print('-------')
print(dic)

# Revisar si existe la llave en el diccionario
if "hero" in dic:
    print(f"El heroe de accion es ") 