from builder import *


import csv

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

import csv

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

def repetir():
        pedido_anterior = input("¿Has realizado un pedido anteriormente? (Sí/No): ")

        if pedido_anterior.lower() == "si":
            # Solicita el nombre del usuario
            nombre_usuario = input("Por favor, introduce tu nombre: ")

            # Busca el nombre en el archivo CSV
            with open('pedidos.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                encontrado = False
                for row in reader:
                    if row and row[0] == nombre_usuario:
                        # Usuario encontrado, muestra sus elecciones pasadas
                        print("¡Bienvenido de nuevo, {}!".format(nombre_usuario))
                        print("Tus elecciones anteriores son:")
                        print(", ".join(row[1:]))
                        encontrado = True
                        print("¿Quieres repetir el pedido?")
                        respuesta = input("Sí/No: ")
                        if respuesta.lower() == "si":
                            # Repite el pedido anterior
                            print("Repetimos el pedido anterior.")
                            pedido = row[1:]
                            break
                            # ...
                            
                        if respuesta.lower() == "no":
                            # Continúa con el proceso de creación de la pizza
                            print("Continúa con el proceso de creación de la pizza.")
                            usuario = Usuario()
                            builder = ConcreteBuilder1()
                            usuario.builder = builder
                        
                            usuario.pedir_nombre()
                            usuario.pedir_contraseña()
                            usuario.pedir_pedido()
                            usuario.pedir_pizza()
                            builder.product_pizza.list_parts()
                            break
            if row and row[0] != nombre_usuario:
                            # Continúa con el proceso de creación de la pizza
                            print("No encontramos tu usuario, continúa con el proceso de creación de la pizza.")
                            usuario = Usuario()
                            builder = ConcreteBuilder1()
                            usuario.builder = builder
                        
                            usuario.pedir_nombre()
                            usuario.pedir_contraseña()
                            usuario.pedir_pedido()
                            usuario.pedir_pizza()
                            builder.product_pizza.list_parts()
                            pass
                            
        else:
                print("Comencemos el proceso de creación de la pizza.")

        # Si el nombre no se encuentra en el archivo CSV o el usuario no ha realizado un pedido anterior
        # Continúa con el proceso de creación de la pizza
                usuario = Usuario()
                builder = ConcreteBuilder1()
                usuario.builder = builder
            
                usuario.pedir_nombre()
                usuario.pedir_contraseña()
                usuario.pedir_pedido()
                usuario.pedir_pizza()
                builder.product_pizza.list_parts()


if __name__ == "__main__":
    """
    El código del cliente crea un objeto constructor, lo pasa al director y luego
     inicia el proceso de construcción. El resultado final se obtiene del
     objeto constructor.
    """
    
    repetir()