# En una funcción el orden de los parametros es importante, por ejemplo:

def print_person_infor(name, age):
    print(f"Persona de nombre {name} y edad {age}")

print_person_infor(age = 18, name = "Seba")
