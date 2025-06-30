# RETO_08
## 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
Se seleccionaron las siguientes funciones:
- Área de un círculo
- Área de un triángulo
- Elevar un número al cubo y restarle 1
```
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
```
## 2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
Se seleccionaron las siguientes funciones:
- Sumatoria de varios números
- Producto de varios números
- Promedio de varios números
```
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
```
## 3. Escriba una función recursiva para calcular la operación de la potencia.
```
def potencia(base: int, exponente: int) -> int:
  if exponente == 0:
    return 1
  return base * potencia(base, exponente - 1)

if __name__ == "__main__":
  b = int(input("Ingrese la base: "))
  e = int(input("Ingrese el exponente: "))
  print("Resultado:", potencia(b, e))
```
## 4. Utilice la siguiente plantilla de code para contar el tiempo:
```
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.

Se hizo el siguiente código para poder probar con distitnos números la diferencia de los resultados:
```
import time

def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Cambiar este número para hacer pruebas
n = 33

# FIBONACCI ITERATIVO
start_time = time.time()
resultado_iter = fibonacci_iterativo(n)
end_time = time.time()
tiempo_iter = end_time - start_time
print(f"[ITERATIVO] Fibonacci({n}) = {resultado_iter}")
print(f"Tiempo iterativo: {tiempo_iter:.6f} segundos")

# FIBONACCI RECURSIVO
start_time = time.time()
resultado_rec = fibonacci_recursivo(n)
end_time = time.time()
tiempo_rec = end_time - start_time
print(f"[RECURSIVO] Fibonacci({n}) = {resultado_rec}")
print(f"Tiempo recursivo: {tiempo_rec:.6f} segundos")

# Pausar para que la consola no se cierre
input("\nPresiona ENTER para salir...")
```
Se realizaron diferentes pruebas y a partir de n = 35, la diferencia en tiempo frente al método iterativo se vuelve notoriamente significativa (pasa de milisegundos a segundos).

Adjunto prueba:
![image](https://github.com/user-attachments/assets/791ff085-64fb-45a5-8609-a53f4ece72f9)

## 5. Crear cuenta en stackoverflow y adjuntar imagen en el repo

Por alguna extraña razón ya la cuenta estaba creada jajaja

![image](https://github.com/user-attachments/assets/3aa496ca-b2b2-4aaf-9267-84d6e3bb0da3)

[Mi perfil de Stack Overflow](https://stackoverflow.com/users/30930825/santiago-ramos-barriga)

## 6. Crear perfil de linkedin

Yo ya tenía una cuenta con mi correo personal, sin embargo acá adjunto imágen y link de mi cuenta ya con el correo institucional.

![image](https://github.com/user-attachments/assets/36f394df-3ba8-43e9-9731-50250d5748d6)

[Mi perfil de LinkedIn](www.linkedin.com/in/santiago-ramos-barriga-00a43b372)
