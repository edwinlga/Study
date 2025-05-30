from productos import Producto


class Movimiento:

    def __init__(self, fecha, tipo, cantidad):
        self.fecha = fecha
        self.tipo = tipo
        self.cantidad = cantidad

    def mostrar_todos():
        pass

    @classmethod
    def agregar(cls, sku, fecha, tipo, cantidad):
        item = Producto.mostrar_por_sku(sku)
        movimientos = item[0]['movimientos']
        print(type(movimientos))
        movimientos.append({
            'palabra': 'hola',
            'otra': 'mas palabras'
            })
        print(movimientos)
        

       


if __name__ == '__main__':
    mov = Movimiento('25/01/2025', 'E', 10)
    mov.agregar(22345678)
