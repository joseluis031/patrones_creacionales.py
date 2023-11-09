from builder import *


import csv

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

import csv

#creame una clase Usuario que pida el nombre del usuario, contraseña y pedido y quiero que para que elija el pedido pase al builder
#y que el builder cree la pizza que el usuario ha pedido


#clase usuario
class Usuario:
    def __init__(self):
         self._builder = None
         self._nombre = None
         self.usuario = None
         self._contrasenia = None
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
    
    #funciones para pedir nombre, usuario, contraseña y pedido
    def pedir_nombre(self) -> None:
        self._nombre = input("Introduzca su nombre: ")
        print("Bienvenido", self._nombre)
        
    def pedir_usuario(self) -> None:
        self._usuario = input("Introduzca su usuario: ")
        print("Usuario correcto")
    
    def pedir_contraseña(self) -> None:
        self._contrasenia = input("Introduzca su contraseña: ")
        print("Contraseña guardada")
        
    def pedir_pedido(self) -> None:
        
        self._pedido = input("¿Quieres realizar un pedido? (si/no) ")
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
        
        #para  guardar el pedido en un csv
        detalles_pizza = builder.product_pizza.parts
        guardar_pedido_en_csv(self._nombre,self._usuario, self._contrasenia, detalles_pizza)

        # Esta función toma los detalles de la pizza y guarda solo las elecciones en un archivo CSV

#funcion para guardar el pedido en un csv   
def guardar_pedido_en_csv(nombre, usuario, contrasenia, detalles):
    with open('pedidosnuevos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        detalles_pizza = [" ".join(detalle.split(":")[1:]) for detalle in detalles]
        writer.writerow([nombre, usuario, contrasenia] + detalles_pizza)


if __name__ == "__main__":
    """
    El código del cliente crea un objeto constructor, lo pasa al director y luego
     inicia el proceso de construcción. El resultado final se obtiene del
     objeto constructor.
    """
    
    #pregunta si el usuario ha realizado un pedido anteriormente
    pedido_anterior = input("¿Has realizado un pedido anteriormente? (si/no): ")

    if pedido_anterior.lower() == "si":
        nombre_usuario = input("Por favor, introduce tu nombre: ")
        nombre_usuario2 = input("Por favor, introduce tu nombre de usuario: ")
        contrasenia = input("Por favor, introduce tu contraseña: ")

        with open('pedidosnuevos.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            encontrado = False
            for row in reader:  #tiene que coincidir el nombre de usuario, el nombre y la contraseña para poder verificar que es cliente
                if row and row[0] == nombre_usuario and row[1] == nombre_usuario2 and row[2] == contrasenia:
                    
                            print("¡Bienvenido de nuevo, {}!".format(nombre_usuario))
                            print("Tus elecciones anteriores son:")
                            #lee y printea los nombre de la columna 0 del csva partir de Masa
                            print("Selecciones: Masa, Salsa, Ingredientes, coccion,presentacion,maridajes,extras")

                            print("Tu pizza: "+ " ".join(row[3:]))
                            print()
                            encontrado = True
                            print("¿Quieres repetir el pedido?")
                            respuesta = input("Sí/No: ")
                            if respuesta.lower() == "si":
                                print("Repetimos el pedido anterior.")
                                pedido = row[3:]
                                break
                            else:
                                print("Comencemos el proceso de creación de la pizza.")
                                usuario = Usuario()
                                builder = ConcreteBuilder1()
                                usuario.builder = builder
                                usuario.pedir_nombre()
                                usuario.pedir_usuario()
                                usuario.pedir_contraseña()
                                usuario.pedir_pedido()
                                usuario.pedir_pizza()
                                builder.product_pizza.list_parts()
                                break

            if not encontrado:
                print("No encontramos tu usuario o la contraseña es incorrecta. Continúa con el proceso de creación de la pizza.")
                usuario = Usuario()
                builder = ConcreteBuilder1()
                usuario.builder = builder
                usuario.pedir_nombre()
                usuario.pedir_usuario()
                usuario.pedir_contraseña()
                usuario.pedir_pedido()
                usuario.pedir_pizza()
                builder.product_pizza.list_parts()

    else:
        print("Comencemos el proceso de creación de la pizza.")
        usuario = Usuario()
        builder = ConcreteBuilder1()
        usuario.builder = builder
        usuario.pedir_nombre()
        usuario.pedir_usuario()
        usuario.pedir_contraseña()
        usuario.pedir_pedido()
        usuario.pedir_pizza()
        builder.product_pizza.list_parts()
        
