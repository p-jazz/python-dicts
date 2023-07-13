# Crear una función que reciba las motas y la información del estudiante e imprima un resumen de su información junto con el promedio de 

def student_result(*grades, **attrs):
    total = 0
    for grade in grades:
        total += grade

    avg = total/len(grades)

    attributes = ""

    for attr in attrs.keys():
        if attr != "name" and attr != "lastname":
            attributes += f"{attr}: {attrs[attr]}"


    print(f"El estudiante {attrs['name']} {attrs['lastname']} con atributos {attributes} tiene promedio {avg}")

student_result(5,6,3,4, name = "Jaz", lastname = "Valladares", sign = "acuario") 
# El estudiante Jaz Valladares con atributos sign: acuario tiene promedio 4.5

student_result(5,3,2, name = "Piero", lastname = "Rojas", sport = "saltar", food = "fideos")

# El estudiante Piero Rojas con atributos sport: saltar tienen promedio 3.3