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

Para ello hemos decidido dividir el csv en 2 csv limpios, uno para la primera relaccion en la que hemos transformado los meses a valores numéricos mediante
un diccionario para establecer la relación del distrito que mas se repite en cada mes a la hora de llamar a las emergencias; y otro hemos creado
una nueva columna en el csv que nos permite saber el tiempo de respuesta de las unidades de emergencia en cada solicitud, y despues hemos calculado la media
del tiempo de respuesta en cada distrito.  (EJERCICIO 1.1)

Cabe decir que a medida que iba desarrollando el patrón, mi entendimiento sobre el mismo, ha ido cambiando por eso tengo otro (EJERCICIO1) incompleto pero
que no he querido borrar para verlo en un futuro y no fallar, en ese patrón en el ejercicio no entendía del todo que tenía que centrarme en el "producto abstracto"
y luego desarrollarlo de diferente manera dependiendo la "ConcretFactory", me daba problemas el hecho de no saber al 100% donde meter cada metodo abstracto

