def leer_temperaturas():
    """
    Función para leer las temperaturas diarias del usuario.
    Retorna una lista de temperaturas.
    """
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura para el día {i+1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número válido.")
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Función para calcular el promedio de una lista de temperaturas.
    Retorna el promedio calculado.
    """
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

def mostrar_resultados(temperaturas, promedio):
    """
    Función para mostrar las temperaturas ingresadas y el promedio calculado.
    """
    print("\nTemperaturas ingresadas:")
    for i, temp in enumerate(temperaturas, start=1):
        print(f"Día {i}: {temp}°C")
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

def main():
    """
    Función principal del programa que organiza el flujo de la ejecución.
    """
    print("Programa para calcular el promedio de temperaturas semanales.")
    temperaturas = leer_temperaturas()
    promedio = calcular_promedio(temperaturas)
    mostrar_resultados(temperaturas, promedio)

# Ejecución del programa
if __name__ == "__main__":
    main()