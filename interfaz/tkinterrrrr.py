import tkinter as tk
from tkinter import messagebox
import csv

class PizzaBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Builder App")
        
        # Variables para almacenar las selecciones del usuario
        self.selections = {
            "nombre_usuario": tk.StringVar(),
            "usuario": tk.StringVar(),
            "contrasenia": tk.StringVar(),
            "tipo_masa": tk.StringVar(),
            "salsa_base": tk.StringVar(),
            "ingredientes_principales": tk.StringVar(),
            "tecnicas_coccion": tk.StringVar(),
            "presentacion": tk.StringVar(),
            "maridajes": tk.StringVar(),
            "extras": tk.StringVar(),
        }

        # Crear la GUI
        self.create_gui()

    def create_gui(self):
        # Etiquetas y entradas para nombre de usuario y contraseña
        self.create_input_entry("Nombre de Usuario:", "nombre_usuario")
        self.create_input_entry("Usuario:", "usuario")
        self.create_input_entry("Contraseña:", "contrasenia", show="*")

        # Etiquetas y entradas de selección
        self.create_selection_entry("Tipo de Masa:", "normal, fina, extrafina, doble", "tipo_masa")
        self.create_selection_entry("Salsa Base:", "tomate, carbonara, barbacoa, pesto", "salsa_base")
        self.create_selection_entry("Ingredientes Principales:", "Separados por comas", "ingredientes_principales")
        self.create_selection_entry("Técnicas de Cocción:", "horno, parrilla, sartén, microondas", "tecnicas_coccion")
        self.create_selection_entry("Presentación:", "cuadrada, redonda, premium, calzone, sorpresa", "presentacion")
        self.create_selection_entry("Maridajes Recomendados:", "cerveza, vino, refresco, agua", "maridajes")
        self.create_selection_entry("Extras:", "queso doble, doble de ingredientes, doble de salsa, trufa, caviar, bordes de queso", "extras")

        # Botón para construir la pizza
        btn_build_pizza = tk.Button(self.root, text="Construir Pizza", command=self.build_pizza)
        btn_build_pizza.pack()

    def create_input_entry(self, label, variable_name, show=None):
        frame = tk.Frame(self.root)
        frame.pack()
        lbl = tk.Label(frame, text=label)
        lbl.pack(side=tk.LEFT)
        entry = tk.Entry(frame, textvariable=self.selections[variable_name], show=show)
        entry.delete(0, tk.END)  # Limpia el campo de entrada
        entry.pack(side=tk.LEFT)

    def create_selection_entry(self, label, placeholder, variable_name):
        frame = tk.Frame(self.root)
        frame.pack()
        lbl = tk.Label(frame, text=label)
        lbl.pack(side=tk.LEFT)
        entry = tk.Entry(frame, textvariable=self.selections[variable_name])
        entry.delete(0, tk.END)  # Limpia el campo de entrada
        entry.insert(0, placeholder)
        entry.pack(side=tk.LEFT)

    def build_pizza(self):
        # Obtener las selecciones del usuario
        detalles_pizza = [f"{label}: {value.get()}" for label, value in self.selections.items()]

        # Guardar las selecciones en un archivo CSV
        with open('pedidos.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(detalles_pizza)

        messagebox.showinfo("Pizza Construida", "¡Pizza construida y guardada en el archivo CSV!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaBuilderApp(root)
    root.mainloop()
