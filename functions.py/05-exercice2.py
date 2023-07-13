

def is_triangle(side1,side2,side3):
    if side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2:
        print("Si se puede hacer un triangulo con esos largos")
    else:
        print("No se puede")

triangle1 = is_triangle(3,4,5)
triangle2 = is_triangle(2,2,15)