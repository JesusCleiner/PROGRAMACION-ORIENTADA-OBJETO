class Botella:
    def __init__(self, capacidad, material):
        self.capacidad = capacidad
        self.material = material
        print(f"Botella de {self.capacidad}ml de {self.material} creada.")

    def __del__(self):
        print(f"Botella de {self.capacidad}ml de {self.material} eliminada.")

class BotellaPlastico(Botella):
    def __init__(self, capacidad, peso_preforma):
        super().__init__(capacidad, "plástico")
        self.peso_preforma = peso_preforma
        print(f"Botella de plástico con preforma de {self.peso_preforma} gramos inicializada.")

    def __del__(self):
        print(f"Botella de plástico de {self.capacidad}ml eliminada.")
        super().__del__()

# Crear instancias de botellas
botella1 = BotellaPlastico(500, 12.8)
botella2 = BotellaPlastico(1000, 22)

# Eliminar referencias a las botellas para desencadenar los destructores
del botella1
del botella2