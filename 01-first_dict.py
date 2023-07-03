# Un diccionario es como una lista, pero más general, es decir, en un diccionario los índices pueden ser casi de cualquier tipo.
# En los diccionarios los indices son llamados *llaves* o *keys* y tiene asociado sus respectivos valores.

# Ejemplos

empty_dict = {} # Crea un diccionario vacío
english_to_spanish = {"one":"uno","two":"dos"} # Crea un diccionario con dos elementos

# Los elementos se agregan en pares, es decir, llave-valor

english_to_spanish["hello"] = "hola"
english_to_spanish["bye"] = "chao"

print(english_to_spanish)

# Para acceder a el valor de una llave en específico usamos la notación con []
print(english_to_spanish["one"])

# El largo de un diccionario se puede obtener con la función len(), igual que con las listas
print(len(english_to_spanish)) # => 4