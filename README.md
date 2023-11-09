# patrones_creacionales.py

El link de este repositorio es el siguiente[GitHub](https://github.com/joseluis031/patrones_creacionales.py.git)


## Ejercicio 1
### Análisis Modular de las Activaciones del SAMUR-Protección Civil en Madrid con Abstract Factory
Para resolver este ejercicio hemos hecho uso de código y csv que explicaré mas adelante
### Código abstract Factory
```
from __future__ import annotations
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt

import pandas as pd

# Clase Abstracta para la fábrica

class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    
    @abstractmethod
    def crear_relacion_mes_distrito(self) -> Abstractmes_distrito: #metodo abstracto
        pass
    
    def crear_relacion_distrito_tiempo_respuesta(self) -> Abstractdistrito_tiempo_respuesta: #metodo abstracto
        pass


    

# Fábrica concreta para datos numéricos

class ConcreteFactory_numerico(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """
    
    '''Cada fábrica concreta derivada de esta interfaz implementará 
    estos métodos para crear instancias de productos relacionados.
    '''


    def crear_relacion_mes_distrito(self) -> Abstractmes_distrito: #metodo abstracto
        return Concretemes_distrito_numerico()   #devuelve el metodo de la clase concreta
    
    def crear_relacion_distrito_tiempo_respuesta(self) -> Abstractdistrito_tiempo_respuesta: #metodo abstracto
        return Concretedistrito_tiempo_respuesta_numerico()         #devuelve el metodo de la clase concreta



# Fábrica concreta para gráficas
class ConcreteFactory_grafica(AbstractFactory):
    """
    Esta clase concreta (ConcreteFactory_numerico) implementa la interfaz AbstractFactory, 
    proporcionando versiones numéricas de los productos 
    (Concretemes_distrito_numerico y Concretedistrito_tiempo_respuesta_numerico).    
    """
    

    def crear_relacion_mes_distrito(self) -> Abstractmes_distrito: #metodo abstracto
        return Concretemes_distrito_grafica()       #devuelve el metodo de la clase concreta
    
    def crear_relacion_distrito_tiempo_respuesta(self) -> Abstractdistrito_tiempo_respuesta: #metodo abstracto
        return Concretedistrito_tiempo_respuesta_grafica()                  #devuelve el metodo de la clase concreta


    

## Clase Abstracta para la relación entre mes y distrito
class Abstractmes_distrito(ABC):
    """
    La interfaz Abstractmes_distrito define un método abstracto 
    moda_mes_distrito que deberá ser implementado por las clases concretas.
    """

    @abstractmethod
    def moda_mes_distrito(self) -> str: #metodo abstracto
        pass
    


"""
Concrete Products are created by corresponding Concrete Factories.
"""

# Clase concreta para relación numérica entre mes y distrito
'''
Esta clase concreta (Concretemes_distrito_numerico) implementa la interfaz 
Abstractmes_distrito para producir una relación 
numérica entre el distrito que más se repite en cada mes.
'''
class Concretemes_distrito_numerico(Abstractmes_distrito): #hereda de la clase abstracta
    def moda_mes_distrito(self,datos) -> str:
        moda = datos.groupby('Distrito')['Mes'].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
        print("Relacion entre Distrito que mas se repite en cada Mes(1=ENERO,2=FEBRERO...): ")
        return moda
    
    
# Clase concreta para relación gráfica entre mes y distrito

'''
Esta otra clase concreta (Concretemes_distrito_grafica) también implementa la interfaz 
Abstractmes_distrito, pero en lugar de devolver 
la relación como solucion numerica, crea y guarda una gráfica.
'''
class Concretemes_distrito_grafica(Abstractmes_distrito):
    def moda_mes_distrito(self,datos) -> str:
        moda = datos.groupby('Distrito')['Mes'].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
        moda.plot(kind='bar', figsize=(10,5))
        #etiquetas
        plt.xlabel('Mes')
        plt.ylabel('Distrito')
        plt.title('Distrito que mas se repite en cada Mes(1=ENERO,2=FEBRERO...)')
        #guardar grafico
        
        plt.savefig('Ejercicio1.1/Graficas/relacion_mes_distrito.png')
        plt.show()
    



## Clase Abstracta para la relación entre distrito y tiempo de respuesta

'''La interfaz Abstractdistrito_tiempo_respuesta define un método abstracto 
media_tiempo_resp_distrito 
que deberá ser implementado por las clases concretas.
'''
class Abstractdistrito_tiempo_respuesta(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def media_tiempo_resp_distrito(self) -> None: #metodo abstracto
        pass




# Clase concreta para relación numérica entre distrito y tiempo de respuesta
'''
Esta clase concreta (Concretedistrito_tiempo_respuesta_numerico) implementa la interfaz 
Abstractdistrito_tiempo_respuesta para calcular 
la media numérica del tiempo de respuesta en cada distrito.
'''
class Concretedistrito_tiempo_respuesta_numerico(Abstractdistrito_tiempo_respuesta): #hereda de la clase abstracta
    def media_tiempo_resp_distrito(self,data) -> str:
        media = data.groupby('Distrito')['Tiempo de respuesta'].mean()
        print("La media del tiempo de respuesta en cada distrito es: ")
        return media

   



# Clase concreta para relación gráfica entre distrito y tiempo de respuesta
'''
Esta otra clase concreta (Concretedistrito_tiempo_respuesta_grafica) también implementa 
la interfaz Abstractdistrito_tiempo_respuesta, pero en 
lugar de devolver la media como dato numerico, crea y guarda una gráfica.
'''
class Concretedistrito_tiempo_respuesta_grafica(Abstractdistrito_tiempo_respuesta): #hereda de la clase abstracta
    def media_tiempo_resp_distrito(self,data) -> str:
        media = data.groupby('Distrito')['Tiempo de respuesta'].mean()

        media.plot(kind='bar', figsize=(10,5))
        #etiquetas
        plt.xlabel('Distrito')
        plt.ylabel('Tiempo de respuesta')
        plt.title('Media del tiempo de respuesta en cada distrito')
        #guardar grafico
        
        plt.savefig('Ejercicio1.1/Graficas/media_tiempo_resp_distrito.png')
        plt.show()

    

# Función para crear la fábrica
'''
Este es el código del cliente. Se le pasa una fábrica concreta y utiliza las interfaces 
Abstractmes_distrito y Abstractdistrito_tiempo_respuesta para 
crear productos relacionados y realizar operaciones sobre ellos.
'''
def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    datos=pd.read_csv("Ejercicio1.1/datoslimpiosnumericos.csv", sep=';', encoding='ISO-8859-1')
    
    data=pd.read_csv("Ejercicio1.1/datoslimpios_tiempo_respuesta.csv", sep=';', encoding='UTF-8')
    relacion1 = factory.crear_relacion_mes_distrito()
    
    relacion2 = factory.crear_relacion_distrito_tiempo_respuesta()

    

    print(f"{relacion1.moda_mes_distrito(datos)}")
    print(f"{relacion2.media_tiempo_resp_distrito(data)}")
```

### Código Samur(para limpiar el csv)

```
import pandas as pd

 

URL = "https://datos.madrid.es/egob/catalogo/300178-12-samur-activaciones.csv"

 

# Leer CSV desde la URL

data = pd.read_csv(URL, sep=';', encoding='UTF-8')

 

#print(data.head())  # Mostrar las primeras filas para visualizar los datos

#print(data.info())  # Mostrar información sobre el DataFrame

#print(data.describe())  # Mostrar estadísticas básicas sobre el DataFrame

#print(data.isnull().sum())  # Mostrar el número de valores nulos en cada columna  

#como mas de la mitad en la columna de Hospital no tienen valor, la elimino

datos = data.drop(['Hospital'], axis=1) 

#print(datos.info())

#para operar mejor paso la hora de solicitud a minutos

#datos['Hora Solicitud'] = pd.to_datetime(datos['Hora Solicitud'])

#datos['Hora Solicitud'] = datos['Hora Solicitud'].dt.hour * 60 + datos['Hora Solicitud'].dt.minute

#print(datos.head()) #no tiene mucho sentido pasar la hora de solicitud a minutos

#print(datos.head())

#quiero ver cuantos distritos diferentes hay

#print(datos['Distrito'].unique())

#print(datos['Código'].unique()) #hay demasiados tiene mas sentido distrito

datos.to_csv('Ejercicio1.1/datoslimpios.csv', sep=';', encoding='UTF-8')

#quiero un grafico de barras con el mes y el distrito

#hazme un grafico de barras con plt
#para ello pasame la columna de Mes a valores numericos, enero = 1, febrero = 2, etc
import csv
meses_a_numeros = {
    'ENERO': 1,
    'FEBRERO': 2,
    'MARZO': 3,
    'ABRIL': 4,
    'MAYO': 5,
    'JUNIO': 6,
    'JULIO': 7,
    'AGOSTO': 8,
    'SEPTIEMBRE': 9,
    'OCTUBRE': 10,
    'NOVIEMBRE': 11,
    'DICIEMBRE': 12
}

datos['Mes'] = datos['Mes'].map(meses_a_numeros)

#print(datos.head())

#datos.to_csv('Ejercicio1.1/datoslimpiosnumericos.csv', sep=';', encoding='UTF-8')


#quiero que a la columna de Hora Intervencion le restes la columna de Hora Solicitud y me pases el resultado a minutos

import datetime as dt
import numpy as np
data['Hora Intervención'] = pd.to_datetime(data['Hora Intervención'])
data['Hora Solicitud'] = pd.to_datetime(data['Hora Solicitud'])

data['Tiempo de respuesta'] = data['Hora Intervención'] - data['Hora Solicitud']

data['Tiempo de respuesta'] = np.where(data['Hora Intervención']< data['Hora Solicitud'], data['Tiempo de respuesta'] + pd.Timedelta(days=1), data['Tiempo de respuesta'])
#corrigeme para que tenga en cuenta cuando es media noche


data['Tiempo de respuesta'] = data['Tiempo de respuesta'].dt.total_seconds() / 60  # Convierte a minutos

#print(data.head())
data = data.dropna()
data.to_csv('Ejercicio1.1/datoslimpios_tiempo_respuesta.csv', sep=';', encoding='UTF-8')


#quiero ver datos nulos de columnas

#print(data.isnull().sum())  # Mostrar el número de valores nulos en cada columna

#quitar filas con datos nulos en Hora Intervencion y Hora Solicitud

datos = data.dropna(subset=['Hora Intervención', 'Hora Solicitud', 'Código', 'Distrito'])

#quitar columna hospital

datos = datos.drop(['Hospital'], axis=1)
#print(datos.isnull().sum())  # Mostrar el número de valores nulos en cada columna

```

### Códgio main

```
from abstract import *

def main():
    
    eleccion =int(input("¿Que fabrica quieres poner en marcha, la numerica(1) o la grafica(2)?"))
    
    if eleccion==1:
    
        print("Ponemos en marcha la fábrica numérica:")
        client_code(ConcreteFactory_numerico())
        print("\n")
    if eleccion==2: 
        print("Ponemos en marcha la fabrica gráfica:")
        client_code(ConcreteFactory_grafica())
        print("\n")

```

### Código Lanzador

```
from main import *

if __name__ == "__main__":
    main()
```

En la resolución de este ejercicio hemos hecho uso de un csv que hemos tenido que limpiar y posteriormente
guardar en csv nuevos para la lectura de sus datos.

En el ejercicio hemos visto adecuada despues de entender el patrón Abstract factory, lo que pedia el ejercicio y
los datos que teniamos que lo mas óptimo era sacar las relaciones que hemos sacado, ya que despues de probar 
una gran cantidad de relaciones, las que hemos elegido representan de manera adecuada lo que queremos por que no hay excesividad de 
variedad en los datos y se entienden bien las gráficas.

Para ello hemos decidido dividir el csv en 2 csv limpios en los que no tenemos valores nulos, uno para la primera relaccion en la que hemos transformado los meses a valores numéricos mediante un diccionario para establecer la relación del distrito que mas se repite en cada mes a la hora de llamar a las emergencias; y otro hemos creado
una nueva columna en el csv que nos permite saber el tiempo de respuesta de las unidades de emergencia en cada solicitud, y despues hemos calculado la media
del tiempo de respuesta en cada distrito.  (EJERCICIO 1.1)

Cabe decir que a medida que iba desarrollando el patrón, mi entendimiento sobre el mismo, ha ido cambiando por eso tengo otro (EJERCICIO1) incompleto pero
que no he querido borrar para verlo en un futuro y no fallar, en ese patrón en el ejercicio no entendía del todo que tenía que centrarme en el "producto abstracto"
y luego desarrollarlo de diferente manera dependiendo la "ConcretFactory", me daba problemas el hecho de no saber al 100% donde meter cada metodo abstracto.

El patrón que he seguido se basa en un abstract factory que tiene 2 metodos abstractos( relación del distrito que mas se repite en cada mes a la hora de llamar a las emergencias y
la media del tiempo de respuesta en cada distrito ) , luego se divide en 2 fabricas, una numerica que nos calcula los métodos abstractos de manera numérica y otra gráfica que nos
calcula los métodos de manera grafica. Las 2 fabricas utilizan las 2 clases abstractas, cada una para su método, esto es lo que mas me costo entender porque pensaba que cada clase abstracta tenia que estar relacionada solo con 1 fabrica.



## Ejercicio 2
### Sistema Integral de Creación y Gestión de Pizzas Gourmet con Almacenamiento en CSV utilizando el Patrón Builder
Para resolver este ejercicio hemos hecho uso de código y csv que explicaré mas adelante

### Código Builder
```
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

#clase abstracta para el builder
class Builder(ABC): 
    """
    La interfaz Builder especifica métodos para crear las diferentes partes de
     los objetos del Producto.
    """

    @property #Este es un decorador que permite acceder al método como si fuera un atributo.
    @abstractmethod
    def product_pizza(self) -> None:
        pass

    @abstractmethod
    def tipo_de_masa(self) -> None:
        pass

    @abstractmethod
    def salsa_base(self) -> None:
        pass

    @abstractmethod
    def ingredientes_principales(self) -> None:
        pass
    
    @abstractmethod
    def tecnicas_de_coccion(self) -> None:
        pass
    
    @abstractmethod
    def presentacion(self) -> None:
        pass
    
    @abstractmethod
    def maridajes_recomendados(self) -> None:
        pass
    
    @abstractmethod
    def extras(self) -> None:
        pass

#clase concreta para el builder
class ConcreteBuilder1(Builder):
    """
    Las clases de Concrete Builder siguen la interfaz de Builder y proporcionan
     Implementaciones específicas de los pasos de construcción. Su programa puede tener
     Varias variaciones de Builders, implementadas de manera diferente.
    """

    def __init__(self) -> None:
        """
        Una nueva instancia de constructor debe contener un objeto de producto en blanco, que es
         utilizado en el montaje posterior.
        """
        self.reset()

    def reset(self) -> None:
        self._product_pizza = Product1()

    @property #Este es un decorador que permite acceder al método como si fuera un atributo.
    def product_pizza(self) -> Product1:
        """
        Se supone que los constructores de hormigón deben proporcionar sus propios métodos(lo llamo igual) para
         recuperando resultados. Esto se debe a que varios tipos de constructores pueden crear
         productos completamente diferentes que no siguen la misma interfaz.
         Por lo tanto, dichos métodos no se pueden declarar en la interfaz base del Constructor.
         (al menos en un lenguaje de programación de tipo estático).

         Generalmente, después de devolver el resultado final al cliente, un constructor
         Se espera que la instancia esté lista para comenzar a producir otro producto.
         Por eso es una práctica habitual llamar al método reset al final de
         el cuerpo del método `getProduct`. Sin embargo, este comportamiento no es obligatorio,
         y puede hacer que sus constructores esperen una llamada de reinicio explícita desde el
         código de cliente antes de deshacerse del resultado anterior.
        """
        product_pizza = self._product_pizza
        self.reset()
        return product_pizza
    #metodos para crear las diferentes partes de los objetos del producto
    
    #creo una lista para cada elemento de la pizza y luego la añado al producto
    #y si el cliente elige un elemento que no esta en la lista le digo que no lo tenemos y que elija otro
    def tipo_de_masa(self) -> None:
        lista_masa = ["normal", "fina", "extrafina", "doble"]
        masa = input("Introduzca el tipo de masa(normal, fina, extrafina o doble): ")
        if masa not in lista_masa:
            print("no tenemos esa masa, Introduzca un tipo de masa valido")
            self.tipo_de_masa()
        else:
            self._product_pizza.add("masa elegida: {}".format(masa))

    def salsa_base(self) -> None:
        lista_salsa = ["tomate", "carbonara", "barbacoa", "pesto", "vegana"]
        salsa = input("Introduzca la salsa base(tomate, carbonara, barbacoa, pesto o vegana): ")
        if salsa not in lista_salsa:
            print("no tenemos esa salsa, Introduzca una salsa valida")
            self.salsa_base()
        else:
            self._product_pizza.add("salsa base elegida: {}".format(salsa))

    #esta funcion utilizo un bucle while para que el cliente pueda elegir mas de un ingrediente
    def ingredientes_principales(self) -> None:
        lista_ingredientes = ["jamon", "queso", "bacon", "champinones", "pimiento", "cebolla", "atun", "aceitunas", "pollo", "carne", "gambas", "anchoas", "salami", "chorizo", "tomate", "maiz", "piña", "rucula"]
    
        # Crea una lista para almacenar los ingredientes elegidos
        ingredientes_elegidos = []
        #
        while True:
            for i, ingrediente in enumerate(lista_ingredientes, 1):
                print(f"{i}. {ingrediente}")
            
            seleccion = input("Introduce el número del ingrediente o '0' si no quieres mas ingredientes: ")
            
            if seleccion == '0':
                break  # Terminar la selección de ingredientes
            
            if seleccion.isdigit():
                indice = int(seleccion)
                if 1 <= indice <= len(lista_ingredientes):
                    ingrediente_elegido = lista_ingredientes[indice - 1]
                    ingredientes_elegidos.append(ingrediente_elegido)
                    print(f"Has elegido: {ingrediente_elegido}")
                else:
                    print("Número de ingrediente no válido. Inténtalo de nuevo.")
            else:
                print("Entrada no válida. Introduce el número del ingrediente o '0' para terminar.")
        
        # Agrega los ingredientes elegidos al producto
        ingredientes_elegidos_str = ", ".join(ingredientes_elegidos)
        self._product_pizza.add("ingredientes principales elegidos: " + ingredientes_elegidos_str)
    
    def tecnicas_de_coccion(self) -> None:
        lista_coccion = ["horno", "parrilla", "sarten", "microondas"]
        coccion = input("Introduzca las tecnicas de coccion(horno, parrilla, sarten o microondas,): ")
        if coccion not in lista_coccion:
            print("no tenemos esa tecnica de coccion, Introduzca una tecnica de coccion valida")
            self.tecnicas_de_coccion()
        else:
            self._product_pizza.add("tecnicas de coccion elegidas: {}".format(coccion))
    
    def presentacion(self) -> None:
        lista_present = ["cuadrada", "redonda", "premium", "calzone", "sorpresa"]
        present=input("Introduzca la presentacion(cuadrada, redonda, premium, calzone o sorpresa): ")
        if present not in lista_present:
            print("no tenemos esa presentacion, Introduzca una presentacion valida")
            self.presentacion()
        else:
            self._product_pizza.add("presentacion elegida: {}".format(present))
        
    def maridajes_recomendados(self) -> None:
        lista_maridaje = ["cerveza", "vino", "refresco", "agua"]
        maridaje = input("Introduzca los maridajes recomendados(cerveza, vino, refresco o agua): ")
        if maridaje not in lista_maridaje:
            print("no tenemos ese maridaje, Introduzca un maridaje valido")
            self.maridajes_recomendados()
        else:
            self._product_pizza.add("maridajes elegidos: {}".format(maridaje))
        
    def extras(self) -> None:#quiero mas extras
        lista_extras = ["queso doble", "doble de ingredientes", "doble de salsa", "trufa", "caviar", "bordes de queso","salsa  ranchera", "salsa de ajo", "salsa de soja", "salsa de yogur", "salsa de curry" ]
    
        # Crea una lista para almacenar los extras elegidos
        extras_elegidos = []
        
        while True:
            print("Elige extras de la lista:")
            for i, extra in enumerate(lista_extras, 1):
                print(f"{i}. {extra}")
            
            seleccion = input("Introduce el número del extra o '0' para terminar: ")
            
            if seleccion == '0':
                break  # Terminar la selección de extras
            
            if seleccion.isdigit():
                indice = int(seleccion)
                if 1 <= indice <= len(lista_extras):
                    extra_elegido = lista_extras[indice - 1]
                    extras_elegidos.append(extra_elegido)
                    print(f"Has elegido: {extra_elegido}")
                else:
                    print("Número de extra no válido. Inténtalo de nuevo.")
            else:
                print("Entrada no válida. Introduce el número del extra o '0' para terminar.")
        
        # Agrega los extras elegidos al producto
        extras_elegidos_str = ", ".join(extras_elegidos)
        self._product_pizza.add("extras elegidos: " + extras_elegidos_str)
            
    
        
    

#clase para el producto
class Product1():
    """
    Tiene sentido utilizar el patrón Builder sólo cuando sus productos sean bastante
     complejos y requieren una configuración extensa.

     A diferencia de otros patrones creacionales, diferentes constructores concretos pueden producir
     productos no relacionados. En otras palabras, es posible que los resultados de varios constructores no
     Sigue siempre la misma interfaz.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None: 
        self.parts.append(part) #añade las partes de la pizza

    def list_parts(self) -> None:
        print(f"El cliente ha elegido su pizza. {', '.join(self.parts)}", end="") #muestra las partes de la pizza


class Director:
    """
    El Director sólo es responsable de ejecutar los pasos de construcción en un
     secuencia determinada. Es útil cuando se producen productos de acuerdo con un
     orden o configuración específica. Estrictamente hablando, la clase Directora es
     Opcional, ya que el cliente puede controlar a los constructores directamente.
    """
     #creo un constructor
    def __init__(self) -> None:
        self._builder = None
    
    #creo un getter y un setter para el constructor
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

    """
   El Director puede construir varias variaciones de productos utilizando el mismo
     pasos de construcción.
    """
    #creo un metodo para construir la pizza
    def build_pizza(self) -> None:
        self.builder.tipo_de_masa()
        self.builder.salsa_base()
        self.builder.ingredientes_principales()
        self.builder.tecnicas_de_coccion()
        self.builder.presentacion()
        self.builder.maridajes_recomendados()
        self.builder.extras()
```

### Código Cliente y Lanzador
```
from builder import *

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
            for row in reader:  #tiene que coincidir el nombre de usuario, el nombre y la contraseña para poder verificar que es el usuario
                if row and row[0] == nombre_usuario and row[1] == nombre_usuario2 and row[2] == contrasenia:
                    
                            print("¡Bienvenido de nuevo, {}!".format(nombre_usuario))
                            #lee y printea los nombre de la columna 0 del csva partir de Masa
                                #   
                            ingredientes = row[3:]
                            masa = ingredientes[0]
                            salsa = ingredientes[1]
                            otros_ingredientes = ingredientes[2:-4]
                            metodo = ingredientes[-4]
                            presentacion = ingredientes[-3]
                            maridaje = ingredientes[-2]
                            ingredientes_extra = ingredientes[-1]

                            resultado = "Tu anterior pedido de pizza:\nMasa: {}\nSalsa: {}\nIngredientes: {}\nMétodo: {}\nPresentación: {}\nMaridaje: {}\nIngredientes extra: {}".format(masa, salsa, "\n".join(otros_ingredientes), metodo, presentacion, maridaje, ingredientes_extra)

                            print(resultado)

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
        
```

En este ejercicio hemos hecho uso del patrón Builder que consta de una clase abstracta, una clase concreta para el builder y una clase para el producto, mas sencillo de implementar que el Abstract factory,
lo hemos adecuado para la construcción de la pizza en una pizzeria y que de como resultado por terminal la opción de elegir
cada elemento de la pizza y su resultado final.

En el codigo del cliente hemos implementado una clase Usuario para mejorar la experiencia del usuario,
la clase da como resultado por terminal algo mas amigable para el cliente, ya que tiene que poner su nombre, usuario y contraseña, antes de realizar su pedido,
y una vez que realiza su pedido, este se guarda en una base de datos de datos la cual almacena nombre,usuario y contraseña, además de su elección de pizza, gracias a una función que 
lleva a cabo la escritura en la base de datos.
El programa también es capaz de una vez que el cliente está en la web, si es un usuario conocido y introduce bien sus datos, es capaz de buscar en la base de datos su elección de pizza
 y le de la opción de repetir el pedido o guardar otro nuevo.

 El programa garantiza la seguridad y privacidad del usuario ya que solamente él, es capaz de acceder a su cuenta si introduce bien sus datos.
 El programa es flexible a la hora de añadir nuevos ingredientes o fórmulas, tiene una amplia compatibilidad de elecciones, da la opción al cliente, de repetir su pedido y tiene una
 "interfaz amigable por terminal"
