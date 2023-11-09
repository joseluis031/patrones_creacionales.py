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
    
 


