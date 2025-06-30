# Sumar varios números
def sumar_n(*args):
  suma = 0
  for num in args:
    suma += num
  return suma

# Multiplicar varios números
def multiplicar_n(*args):
  resultado = 1
  for num in args:
    resultado *= num
  return resultado

# Calcular promedio
def promedio_n(*args):
  if len(args) == 0:
    return 0
  suma = sumar_n(*args)
  return suma / len(args)

print("Suma:", sumar_n(2, 3, 5))
print("Multiplicación:", multiplicar_n(2, 3, 4))
print("Promedio:", promedio_n(3, 4, 5, 6))