# En el contexto de la programación las funciones son una secuencia 


# Podemos definir nuevas funciones para especificar un nombre junto con una secuencia de sentencias que se ejecutan cuando la función es "llamada, " ejecutar" y 

verses = ["Mano hacia el frente", "Puño cerrado", "Dedo hacia arriba", "Lengua afuera"]

def intro():
    print("Atención, compañia")

def chorus():
    print("Chuchuwa, chuchuwa, chuchu wa wa wa")
    print("Chuchuwa, chuchuwa, chuchu wa wa wa")

def outro():
    print("Lalala lalala la la la la")
    print("Lalala lalala la la la la")

for verse in verses:
    intro()
    print(verse)
    if verse != verses[-1]:
        chorus()
    else:
         outro()
    print("----------")
