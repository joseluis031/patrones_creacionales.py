from builder import *


import csv

director = Director()
builder = ConcreteBuilder1()
director.builder = builder

import csv

def guardar_pedido_en_csv(nombre, usuario,contrasenia,detalles):
    with open('pedidosnuevos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Solo guarda los valores, sin etiquetas
        writer.writerow([nombre,usuario,contrasenia *[" ".join(detalle.split(":")[1:]) for detalle in detalles]])



#creame una clase Usuario que pida el nombre del usuario, contraseña y pedido y quiero que para qe elija el pedido pase al builder
#y que el builder cree la pizza que el usuario ha pedido

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
        guardar_pedido_en_csv(self._nombre,self._usuario, self._contrasenia, detalles_pizza)

        # Esta función toma los detalles de la pizza y guarda solo las elecciones en un archivo CSV
def guardar_pedido_en_csv(nombre,usuario,contrasenia, detalles):
    with open('pedidosnuevos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Solo guarda los valores, sin etiquetas
        writer.writerow([nombre,usuario,contrasenia, *[" ".join(detalle.split(":")[1:]) for detalle in detalles]])


'''import tkinter as tk
from tkinter import ttk

class PizzaBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Builder App")
        
        self.create_widgets()
        self.pizza = []

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="¡Bienvenido a Pizza Builder!")
        self.label.pack(pady=10)
        
        self.masa_label = ttk.Label(self.root, text="Elige el tipo de masa:")
        self.masa_label.pack()
        
        self.masa_var = tk.StringVar()
        self.masa_combobox = ttk.Combobox(self.root, textvariable=self.masa_var)
        self.masa_combobox['values'] = ["Normal", "Fina", "Extrafina", "Doble"]
        self.masa_combobox.pack()
        
        self.salsa_label = ttk.Label(self.root, text="Elige la salsa base:")
        self.salsa_label.pack()
        
        self.salsa_var = tk.StringVar()
        self.salsa_combobox = ttk.Combobox(self.root, textvariable=self.salsa_var)
        self.salsa_combobox['values'] = ["Tomate", "Carbonara", "Barbacoa", "Pesto"]
        self.salsa_combobox.pack()
        
        self.ingredientes_label = ttk.Label(self.root, text="Elige los ingredientes principales:")
        self.ingredientes_label.pack()
        
        self.ingredientes_var = tk.StringVar()
        self.ingredientes_combobox = ttk.Combobox(self.root, textvariable=self.ingredientes_var)
        self.ingredientes_combobox['values'] = ["Jamon", "Queso", "Bacon", "Champiñones", "Pimiento", "Cebolla", "Atun", "Aceitunas", "Pollo", "Carne", "Gambas", "Anchoas", "Salami", "Chorizo", "Tomate", "Maiz", "Piña", "Rucula"]
        self.ingredientes_combobox.pack()
        
        self.coccion_label = ttk.Label(self.root, text="Elige las tecnicas de coccion:")
        self.coccion_label.pack()
        
        self.coccion_var = tk.StringVar()
        self.coccion_combobox = ttk.Combobox(self.root, textvariable=self.coccion_var)
        self.coccion_combobox['values'] = ["Horno", "Parrilla", "Sarten", "Microondas"]
        self.coccion_combobox.pack()
        
        self.presentacion_label = ttk.Label(self.root, text="Elige la presentacion:")
        self.presentacion_label.pack()
        
        self.presentacion_var = tk.StringVar()
        self.presentacion_combobox = ttk.Combobox(self.root, textvariable=self.presentacion_var)
        self.presentacion_combobox['values'] = ["Cuadrada", "Redonda", "Premium", "Calzone", "Sorpresa"]
        self.presentacion_combobox.pack()
        
        self.maridaje_label = ttk.Label(self.root, text="Elige los maridajes recomendados:")
        self.maridaje_label.pack()
        
        self.maridaje_var = tk.StringVar()
        self.maridaje_combobox = ttk.Combobox(self.root, textvariable=self.maridaje_var)
        self.maridaje_combobox['values'] = ["Cerveza", "Vino", "Refresco", "Agua"]
        self.maridaje_combobox.pack()
        
        self.extras_label = ttk.Label(self.root, text="Elige los extras:")
        self.extras_label.pack()
        
        self.extras_var = tk.StringVar()
        self.extras_combobox = ttk.Combobox(self.root, textvariable=self.extras_var)
        self.extras_combobox['values'] = ["Queso doble", "Doble de ingredientes", "Doble de salsa", "Trufa", "Caviar", "Bordes de queso"]
        self.extras_combobox.pack()
        

        self.add_button = ttk.Button(self.root, text="Añadir a la pizza", command=self.add_to_pizza)
        self.add_button.pack(pady=10)

        self.show_pizza_button = ttk.Button(self.root, text="Mostrar detalles de la pizza", command=self.show_pizza)
        self.show_pizza_button.pack()

    def add_to_pizza(self):
        masa = self.masa_var.get()
        salsa = self.salsa_var.get()
        ingredientes = self.ingredientes_var.get()
        coccion = self.coccion_var.get()
        presentacion = self.presentacion_var.get()
        maridaje = self.maridaje_var.get()
        extras = self.extras_var.get()
        
        self.pizza.append(f"Masa: {masa}, Salsa: {salsa}, Ingredientes: {ingredientes}, Tecnicas de coccion: {coccion}, Presentacion: {presentacion}, Maridajes recomendados: {maridaje}, Extras: {extras}")
        self.masa_var.set("")
        self.salsa_var.set("")

    def show_pizza(self):
        pizza_details = "\n".join(self.pizza)
        if pizza_details:
            pizza_details = "Detalles de la pizza:\n" + pizza_details
        else:
            pizza_details = "La pizza está vacía. ¡Elige masa y salsa primero!"
        self.show_message("Detalles de la Pizza", pizza_details)

    def show_message(self, title, message):
        popup = tk.Toplevel()
        popup.title(title)
        label = ttk.Label(popup, text=message)
        label.pack(padx=10, pady=10)
        close_button = ttk.Button(popup, text="Cerrar", command=popup.destroy)
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaBuilderApp(root)
    root.mainloop()

'''


if __name__ == "__main__":
    """
    El código del cliente crea un objeto constructor, lo pasa al director y luego
     inicia el proceso de construcción. El resultado final se obtiene del
     objeto constructor.
    """
    
    
    pedido_anterior = input("¿Has realizado un pedido anteriormente? (Sí/No): ")

    if pedido_anterior.lower() == "si":
        nombre_usuario = input("Por favor, introduce tu nombre: ")
        nombre_usuario2 = input("Por favor, introduce tu nombre de usuario: ")
        contrasenia = input("Por favor, introduce tu contraseña: ")

        with open('pedidos.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            encontrado = False
            for row in reader:
                if row and row[0] == nombre_usuario:
                    
                            print("¡Bienvenido de nuevo, {}!".format(nombre_usuario))
                            print("Tus elecciones anteriores son:")
                            print(", ".join(row[1:]))
                            encontrado = True
                            print("¿Quieres repetir el pedido?")
                            respuesta = input("Sí/No: ")
                            if respuesta.lower() == "si":
                                print("Repetimos el pedido anterior.")
                                pedido = row[3:]
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