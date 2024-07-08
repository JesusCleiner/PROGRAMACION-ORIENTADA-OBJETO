class OrdenProduccion:
    def __init__(self, molde, gramaje, cantidad_producir, embalaje):
        self.molde = molde
        self.gramaje = gramaje
        self.cantidad_producir = cantidad_producir
        self.embalaje = embalaje

    def mostrar_detalles(self):
        print(f"Molde: {self.molde}, Gramaje: {self.gramaje}g, Cantidad a producir: {self.cantidad_producir}, Embalaje: {self.embalaje} botellas por bulto")

class IngresoBodega:
    def __init__(self, descripcion, cantidad_por_bulto, cantidad_bultos):
        self.descripcion = descripcion
        self.cantidad_por_bulto = cantidad_por_bulto
        self.cantidad_bultos = cantidad_bultos

    def mostrar_detalles(self):
        print(f"Descripción: {self.descripcion}, Cantidad por bulto: {self.cantidad_por_bulto}, Cantidad de bultos: {self.cantidad_bultos}")

class Botella(OrdenProduccion, IngresoBodega):
    def __init__(self, molde, gramaje, cantidad_producir, embalaje, descripcion, cantidad_por_bulto, cantidad_bultos):
        OrdenProduccion.__init__(self, molde, gramaje, cantidad_producir, embalaje)
        IngresoBodega.__init__(self, descripcion, cantidad_por_bulto, cantidad_bultos)

    def mostrar_detalles(self):
        print("Detalles de Producción:")
        OrdenProduccion.mostrar_detalles(self)
        print("Detalles de Ingreso a Bodega:")
        IngresoBodega.mostrar_detalles(self)

# Crear instancia de Botella
if __name__ == "__main__":
    molde = input("Ingrese el molde a utilizar (ej. 300ml, 500ml, 1000ml): ")
    gramaje = float(input("Ingrese el gramaje de la preforma (en gramos): "))
    cantidad_producir = int(input("Ingrese la cantidad de botellas a producir: "))
    embalaje = int(input("Ingrese la cantidad de botellas por bulto: "))
    
    descripcion = input("Ingrese la descripción de la botella: ")
    cantidad_por_bulto = int(input("Ingrese la cantidad de botellas por bulto: "))
    cantidad_bultos = int(input("Ingrese la cantidad de bultos a ingresar a bodega: "))

    botella = Botella(molde, gramaje, cantidad_producir, embalaje, descripcion, cantidad_por_bulto, cantidad_bultos)
    botella.mostrar_detalles()