from tabulate import tabulate
from data.db_productos import productos


class Producto:

    def __init__(self, sku, categoria, nombre, descripcion, precio_unitario, cantidad_bodega):

        # ::::::::::: Aplicando la programacion defensiva :::::::::::

        # Validando que no haya parametros vacios o None
        if not all([sku, categoria, nombre, descripcion, precio_unitario, cantidad_bodega]):
            return 0

        # Validando que precio_unitario sea numerico
        if not isinstance(precio_unitario, (int, float)) or precio_unitario <= 0:
            return 0

        # Validando que cantida_bodega sea numerico e igual o mayor que cero
        if not isinstance(precio_unitario, (int, float)) or precio_unitario <= 0:
            return 0

        self.sku = sku
        self.categoria = categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.cantidad_bodega = cantidad_bodega
        # Movimientos
        self.movimientos = []

    def agregar(self):

        productos.append({
            'sku': self.sku,
            'categoria': self.categoria,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio_unitario': self.precio_unitario,
            'cantidad_bodega': self.cantidad_bodega

        })

    @classmethod
    def existe_sku(cls, sku):
        "Comprueba si el SKU ya ha sido asignado a un producto"
        lista_sku = [p['sku'] for p in productos]
        return sku in lista_sku

    @classmethod
    def mostrar_por_sku(cls, sku):
        "Mostrar productos por SKU"
        if Producto.existe_sku(sku):
            detalles = [p.values() for p in productos if p['sku'] == sku]
            print(detalles)
            #print(tabulate([['SKU', 'CATEGORIA', 'NOMBRE', 'DESCRIPCION', 'PRECIO', 'CANTIDAD', 'MOVIMIENTOS'], detalles], headers='firstrow'))
        else:
            return None

    @classmethod
    def mostrar_listado(cls):
      listado=[
        ['SKU', 'CATEGORIA', 'NOMBRE', 'DESCRIPCION', 'PRECIO', 'CANTIDAD', 'MOVIMIENTOS']
      ]
      for p in productos:
        listado.append(p.values())
      
      print(tabulate(listado, headers='firstrow'))



if __name__ == "__main__":

    producto = Producto(10345678, 'Herramientas', 'Alicate',
                        'Alicate de electricista', 150, 20)
    producto.agregar()
    #Producto.mostrar_listado()
    Producto.mostrar_por_sku(10345678)
    
