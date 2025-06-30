def potencia(base: int, exponente: int) -> int:
  if exponente == 0:
    return 1
  return base * potencia(base, exponente - 1)

if __name__ == "__main__":
  b = int(input("Ingrese la base: "))
  e = int(input("Ingrese el exponente: "))
  print("Resultado:", potencia(b, e))