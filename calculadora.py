def area_cuadrado(lado):
    return lado * lado

if __name__ == "__main__":
    print("=== Calculadora de Área (Versión 1: Cuadrado) ===")
    lado = float(input("Ingrese el lado del cuadrado: "))
    print(f"El área del cuadrado es: {area_cuadrado(lado)}")
