# Clase Botella representa una botella de plástico con un tamaño específico y peso de preforma.
class Botella:
    def __init__(self, capacidad_ml, peso_preforma_g, es_transparente=True):
        # Atributos de la clase Botella
        self.capacidad_ml = capacidad_ml  # Capacidad de la botella en mililitros
        self.peso_preforma_g = peso_preforma_g  # Peso de la preforma en gramos
        self.es_transparente = es_transparente  # Si la botella es transparente

    def descripcion(self):
        # Método que devuelve una descripción de la botella
        return (f"Botella de {self.capacidad_ml}ml, "
                f"preforma de {self.peso_preforma_g}g, "
                f"{'transparente' if self.es_transparente else 'no transparente'}")

# Clase Pedido representa un pedido de varias botellas
class Pedido:
    def __init__(self, id_pedido, cliente):
        # Atributos de la clase Pedido
        self.id_pedido = id_pedido  # Identificador del pedido
        self.cliente = cliente  # Cliente que realiza el pedido
        self.botellas = {}  # Diccionario para almacenar las botellas y sus cantidades en el pedido

    def agregar_botella(self, botella, cantidad):
        # Método para agregar una botella al pedido
        if botella in self.botellas:
            self.botellas[botella] += cantidad
        else:
            self.botellas[botella] = cantidad
        print(f"Agregadas {cantidad} unidades de {botella.descripcion()} al pedido {self.id_pedido} del cliente {self.cliente}")

    def resumen_pedido(self):
        # Método para mostrar un resumen del pedido
        print(f"Resumen del pedido {self.id_pedido} para {self.cliente}:")
        for botella, cantidad in self.botellas.items():
            print(f"{cantidad} unidades de {botella.descripcion()}")

# Creación de botellas con diferentes capacidades y pesos de preforma
botella_300ml = Botella(300, 12.8)
botella_400ml = Botella(400, 12.8)
botella_500ml = Botella(500, 12.8)
botella_1000ml = Botella(1000, 22)

# Creación de un pedido para un cliente
pedido_1 = Pedido(1, "Cliente A")

# Ingresar la cantidad de botellas a vender por teclado
cantidades = {}
cantidades['300ml'] = int(input("Ingrese la cantidad de botellas de 300ml: "))
cantidades['400ml'] = int(input("Ingrese la cantidad de botellas de 400ml: "))
cantidades['500ml'] = int(input("Ingrese la cantidad de botellas de 500ml: "))
cantidades['1000ml'] = int(input("Ingrese la cantidad de botellas de 1000ml: "))

# Agregar botellas al pedido
pedido_1.agregar_botella(botella_300ml, cantidades['300ml'])
pedido_1.agregar_botella(botella_400ml, cantidades['400ml'])
pedido_1.agregar_botella(botella_500ml, cantidades['500ml'])
pedido_1.agregar_botella(botella_1000ml, cantidades['1000ml'])

# Mostrar el resumen del pedido
pedido_1.resumen_pedido()

