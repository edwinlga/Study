class ConsoleMenu:

    def __init__(self, title:str, options:list):
        self.title = title
        self.options = options

    def display(self):
        words_lengths = [len(p) for p in self.options]
        words_lengths.append(len(self.title))
        width = max(words_lengths)+4
        margin_title = (width-len(self.title))//2
        
        print("="*width)
        print((" "*margin_title + self.title))
        print("="*width)
        for option in list(enumerate(self.options, start=1)):
            print(f"{option[0]}.- {option[1]}")
        print(f"0.- Salir")
        print("="*width)

    def get_option(self):
        selection = int(input(" Seleccione una opcion del menu: "))
        if not 0<= selection <= len(self.options) or not isinstance(selection, int):
            print("Debe seleccionar una opcion valida. Intente de nuevo.")
        return selection
    
if __name__ == '__main__':
    menu = ConsoleMenu("Menu Principal", ["Crear producto", "Catalogo de productos", "Producto por SKU", "Movimientos"])
    menu.display()
    print(menu.get_option())
    
