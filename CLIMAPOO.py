class Clima:
    def __init__(self):
        self._temperaturas = []  # Encapsulamiento: lista de temperaturas protegida

    def ingresar_temperatura(self, temperatura):
        """
        Método para ingresar la temperatura diaria.
        """
        if not isinstance(temperatura, (int, float)):
            raise ValueError("La temperatura debe ser un número.")
        self._temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        """
        Método para calcular el promedio semanal de temperaturas.
        """
        if not self._temperaturas:
            raise ValueError("No hay temperaturas ingresadas.")
        total = sum(self._temperaturas)
        promedio = total / len(self._temperaturas)
        return promedio

    def mostrar_temperaturas(self):
        """
        Método para mostrar las temperaturas ingresadas.
        """
        print("\nTemperaturas ingresadas:")
        for i, temp in enumerate(self._temperaturas, start=1):
            print(f"Día {i}: {temp}°C")


class ClimaDetallado(Clima):
    def __init__(self):
        super().__init__()
        self._detalles = []  # Lista para almacenar detalles adicionales del clima

    def ingresar_detalle(self, temperatura, detalle):
        """
        Método para ingresar la temperatura y un detalle adicional.
        """
        super().ingresar_temperatura(temperatura)
        self._detalles.append(detalle)

    def mostrar_temperaturas_y_detalles(self):
        """
        Método para mostrar las temperaturas y los detalles adicionales.
        """
        print("\nTemperaturas y detalles ingresados:")
        for i, (temp, detalle) in enumerate(zip(self._temperaturas, self._detalles), start=1):
            print(f"Día {i}: {temp}°C - Detalle: {detalle}")


def main():
    """
    Función principal del programa.
    """
    clima_semanal = ClimaDetallado()
    print("Programa para calcular el promedio de temperaturas semanales con detalles adicionales.")
    
    for dia in range(1, 8):
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura para el día {dia}: "))
                detalle = input(f"Ingrese un detalle adicional para el día {dia}: ")
                clima_semanal.ingresar_detalle(temperatura, detalle)
                break
            except ValueError as e:
                print(f"Error: {e}. Intente de nuevo.")

    clima_semanal.mostrar_temperaturas_y_detalles()
    promedio = clima_semanal.calcular_promedio_semanal()
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

# Ejecución del programa
if __name__ == "__main__":
    main()