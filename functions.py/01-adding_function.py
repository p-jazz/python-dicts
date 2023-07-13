from time import sleep
# En el contexto de la programación las funciones son una secuencia de sentencias de codigo con un nombre.
# Se parecen en algo a las variables en el sentido de qu son un simple nombre. En el caso delas variables, estas apuntan a un valor, mientras que en el caso de las funciones, apuntan a una serie de sentencias que realizan una tarea especifica.

# Python trae varias funciones ya listas como las clasicas print(), int(), len(), etc

# Podemos definir nuevas funciones para especificar un nombre junto con una secuencia de sentencias que se ejecutan cuando la función es "llamada, " ejecutada" o "invocada" 

# Algunas funciones puden requerir agumentos. Por ejemplo print() recibe como argumento lo que va a imprimir en la terminal. Algunas funciones reciben más de un argumento.

# Un detalle es que cuando estamps dentro de la función los arumenyos se asignan a variables locales llamadas  **parámetros**. Profundizaremos más adelante

verses = ["Mano hacia el frente", "Puño cerrado", "Dedo hacia arriba", "Lengua afuera"]

def intro(verse):
    print(f"Atención, compañia: {verse}")
    sleep(1)

def chorus():
    print("Chuchuwa") 
    sleep(1)
    print("Chuchuwa")
    sleep(1)
    print("Chuchuwa")
    sleep(0.8)
    print("wa wa wa")

def outro():
    print("Lalala lalala la la la la")
    print("Lalala lalala la la la la")

for verse in verses:
    intro(verse)
    # Esto revisa si el verso NO es el ultimo de los versos
    if verse != verses[-1]:
        chorus()
    else:
         outro()
    print("----------")
