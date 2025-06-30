# Area de un círculo
area_circulo = lambda r: 3.1416 * r**2
print("Área del círculo con radio 4:", area_circulo(4))

# Area de un triangulo
area_triangulo = lambda b, h: (b * h) / 2
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
print(f"Área del triángulo: {area_triangulo(base, altura)}")

# Evaluar f(x) = x * x^(1/3) - 1
funcion_f = lambda x: x * (x**(1/3)) - 1
print("f(8):", funcion_f(8))