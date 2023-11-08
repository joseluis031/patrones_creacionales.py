from __future__ import annotations
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt

import pandas as pd
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
    def crear_relacion_mes_distrito(self) -> Abstractmes_distrito:
        pass
    
    def crear_relacion_distrito_tiempo_respuesta(self) -> Abstractdistrito_tiempo_respuesta:
        pass


    



class ConcreteFactory_numerico(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def crear_relacion_mes_distrito(self) -> Abstractmes_distrito:
        return Concretemes_distrito_numerico()
    
    def crear_relacion_distrito_tiempo_respuesta(self) -> Abstractdistrito_tiempo_respuesta:
        return Concretedistrito_tiempo_respuesta_numerico()




class ConcreteFactory_grafica(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def crear_relacion_mes_distrito(self) -> Abstractmes_distrito:
        return Concretemes_distrito_grafica()
    
    def crear_relacion_distrito_tiempo_respuesta(self) -> Abstractdistrito_tiempo_respuesta:
        return Concretedistrito_tiempo_respuesta_grafica()


    


class Abstractmes_distrito(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def moda_mes_distrito(self) -> str:
        pass
    


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class Concretemes_distrito_numerico(Abstractmes_distrito):
    def moda_mes_distrito(self,datos) -> str:
        moda = datos.groupby('Distrito')['Mes'].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
        print("Relacion entre Distrito que mas se repite en cada Mes(1=ENERO,2=FEBRERO...): ")
        return moda
    
    

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
    




class Abstractdistrito_tiempo_respuesta(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def media_tiempo_resp_distrito(self) -> None:
        pass





class Concretedistrito_tiempo_respuesta_numerico(Abstractdistrito_tiempo_respuesta):
    def media_tiempo_resp_distrito(self,data) -> str:
        media = data.groupby('Distrito')['Tiempo de respuesta'].mean()
        print("La media del tiempo de respuesta en cada distrito es: ")
        return media

   




class Concretedistrito_tiempo_respuesta_grafica(Abstractdistrito_tiempo_respuesta):
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
    
 


