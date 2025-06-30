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

