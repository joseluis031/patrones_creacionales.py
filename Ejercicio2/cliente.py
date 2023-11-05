from builder import *


import csv

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

# Esta función toma los detalles de la pizza y los guarda en un archivo CSV
def guardar_pedido_en_csv(nombre, detalles):
    with open('pedidos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, *detalles])

#creame una clase Usuario que pida el nombre del usuario, contraseña y pedido y quiero que para qe elija el pedido pase al builder
#y que el builder cree la pizza que el usuario ha pedido

class Usuario:
    def __init__(self):
         self._builder = None
         self._nombre = None
         self._contraseña = None
         self._pedido = None
         self._pizza = None

    @property
    def builder(self) -> Builder:
         return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
         """
         El Director trabaja con cualquier instancia de constructor que pase el código del cliente.
          lo. De esta manera, el código del cliente puede alterar el tipo final del nuevo
          producto ensamblado.
         """
         self._builder = builder
            
    def pedir_nombre(self) -> None:
        self._nombre = input("Introduzca su nombre: ")
        print("Bienvenido", self._nombre)
    
    def pedir_contraseña(self) -> None:
        self._contraseña = input("Introduzca su contraseña: ")
        print("Contraseña correcta")
        
    def pedir_pedido(self) -> None:
        
        self._pedido = input("¿Quieres realizar un pedido? (S/N) ")
        if self._pedido == "Si" or "si" or "S" or "s":
            print("Vamos a ello!!")
        
        
    def pedir_pizza(self) -> None:
        self.builder.tipo_de_masa()
        self.builder.salsa_base()
        self.builder.ingredientes_principales()
        self.builder.tecnicas_de_coccion()
        self.builder.presentacion()
        self.builder.maridajes_recomendados()
        self.builder.extras()
    
        detalles_pizza = builder.product_pizza.parts
        guardar_pedido_en_csv(self._nombre, detalles_pizza)

# Esta función toma los detalles de la pizza y guarda solo las elecciones en un archivo CSV
def guardar_pedido_en_csv(nombre, detalles):
    with open('pedidos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Solo guarda los valores, sin etiquetas
        writer.writerow([nombre, *[" ".join(detalle.split(":")[1:]) for detalle in detalles]])



if __name__ == "__main__":
    """
    El código del cliente crea un objeto constructor, lo pasa al director y luego
     inicia el proceso de construcción. El resultado final se obtiene del
     objeto constructor.
    """
    
    usuario1 = Usuario()
    builder = ConcreteBuilder1()
    usuario1.builder = builder
    
    usuario1.pedir_nombre()
    usuario1.pedir_contraseña()
    usuario1.pedir_pedido()
    usuario1.pedir_pizza()
    builder.product_pizza.list_parts()
    
    
    print("\n")
    
    usuario2 = Usuario()
    builder = ConcreteBuilder1()
    usuario2.builder = builder
    
    usuario2.pedir_nombre()
    usuario2.pedir_contraseña()
    usuario2.pedir_pedido()
    usuario2.pedir_pizza()
    builder.product_pizza.list_parts()
    
    print("\n")
    
    usuario3 = Usuario()
    builder = ConcreteBuilder1()
    usuario3.builder = builder

    usuario3.pedir_nombre()
    usuario3.pedir_contraseña()
    usuario3.pedir_pedido()
    usuario3.pedir_pizza()
    builder.product_pizza.list_parts()
    

    