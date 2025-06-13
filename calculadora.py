def area_cuadrado(lado):
    return lado * lado

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

if __name__ == "__main__":
    print("=== Calculadora de Área (Versión 3: Cuadrado + Triángulo + Rectángulo) ===")
    print("1. Cuadrado\n2. Triángulo\n3. Rectángulo")
    opcion = int(input("Seleccione figura (1-3): "))

    if opcion == 1:
        lado = float(input("Ingrese el lado del cuadrado: "))
        print(f"Área del cuadrado: {area_cuadrado(lado)}")
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print(f"Área del triángulo: {area_triangulo(base, altura)}")
    elif opcion == 3:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print(f"Área del rectángulo: {area_rectangulo(base, altura)}")
    else:
        print("Opción no válida")