from data.db_productos import productos

class Producto:

  def __init__(self, sku, categoria, nombre, descripcion, precio_unitario, cantidad_bodega):

    # ::::::::::: Aplicando la programacion defensiva :::::::::::

    # Validando que no haya parametros vacios o None
    if not all([sku, categoria,nombre,descripcion,precio_unitario,cantidad_bodega]):
      return 0

    # Validando que precio_unitario sea numerico
    if not isinstance(precio_unitario, (int, float)) or precio_unitario <= 0:
      return 0

    # Validando que cantida_bodega sea numerico e igual o mayor que cero
    if not isinstance(precio_unitario, (int, float)) or precio_unitario <= 0:
      return 0

    self.sku=sku
    self.categoria=categoria
    self.nombre=nombre
    self.descripcion=descripcion
    self.precio_unitario=precio_unitario
    self.cantidad_bodega=cantidad_bodega
    # Movimientos
    self.movimientos=[]

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
    lista_sku =[p['sku'] for p in productos]
    return sku in lista_sku


  @classmethod
  def mostrar_por_sku(cls, sku):
    "Mostrar productos por SKU"
    if Producto.existe_sku(sku):
      return [p for p in productos if p['sku']==sku]
    else:
      return None

  
if __name__ == "__main__":
  print(Producto.mostrar_por_sku(22345678))