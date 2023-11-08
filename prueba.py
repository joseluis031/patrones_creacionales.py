import matplotlib.pyplot as plt

# Datos de ejemplo: tipos de pizza y cantidad de pedidos
tipos_de_pizza = ["Margarita", "Pepperoni", "Hawaiana", "Vegetariana"]
cantidad_pedidos = [20, 35, 15, 28]

# Crear un objeto de figura
fig, ax = plt.subplots()

# Crear el gráfico de barras
ax.bar(tipos_de_pizza, cantidad_pedidos, color='royalblue')

# Personalizar el gráfico
ax.set_xlabel('Tipos de Pizza')
ax.set_ylabel('Cantidad de Pedidos')
ax.set_title('Comparación de Pedidos de Pizza')

# Mostrar el gráfico
plt.show()
