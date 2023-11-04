from __future__ import annotations
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt

import pandas as pd


class AbstractFactory(ABC):
    """
    La interfaz Abstract Factory declara un conjunto de métodos que devuelven
     diferentes productos abstractos. Estos productos se llaman familia y son
     relacionados por un tema o concepto de alto nivel. Los productos de una familia suelen ser
     capaces de colaborar entre sí. Una familia de productos puede tener varios
     variantes, pero los productos de una variante son incompatibles con los productos de
     otro.
    """
    @abstractmethod
    def analisis_estadistico(self) -> AbstractProductA:
        pass
    
    """
    Creo las 2 funciones que me pide el ejercicio en abstract y luego en concrete ire desarrollandolas 1 a 1
    """
    @abstractmethod
    def visualizaciones_graficas(self) -> AbstractProductB:
        pass
    


class ConcreteFactory1(AbstractFactory):
    """
    Las Fábricas de Hormigón producen una familia de productos que pertenecen a un solo
     variante. La fábrica garantiza que los productos resultantes son compatibles. Nota
     que las firmas de los métodos de Concrete Factory devuelven un resumen
     producto, mientras que dentro del método se instancia un producto concreto.
    """

    def analisis_estadistico(self) -> AbstractProductA:
        return ConcreteProductA1()


class ConcreteFactory2(AbstractFactory):
    """
    Cada fábrica de hormigón tiene una variante de producto correspondiente.
    """

    def visualizaciones_graficas(self) -> AbstractProductB:
        return ConcreteProductB2()
    


class AbstractProductA(ABC):
    """
    Cada producto distinto de una familia de productos debe tener una interfaz base. Todo
     Las variantes del producto deben implementar esta interfaz.
    """
    '''
    Aqui creo las 3 funciones (dentro del analisis que llevare a cabo en la fabrica 1)
    que me pide el ejercicio en abstract y luego en concrete ire desarrollandolas 1 a 1
    '''
    @abstractmethod
    def media(self) -> str:
        pass
    '''
    @abstractmethod
    def another_useful_function_a(self, collaborator: AbstractProductB) -> str:
        pass
    '''
    @abstractmethod
    def moda(self) -> str:
        pass
    
    @abstractmethod
    def mediana(self) -> str:
        pass
    

"""
Los productos de hormigón son creados por las correspondientes fábricas de hormigón.
"""


class ConcreteProductA1(AbstractProductA):
    def media(self, datos) -> str:
        
        return "La media es: " + str(datos.mean())
    '''
    def another_useful_function_a(self, collaborator: AbstractProductB) -> str:
        """
        La variante, Producto A1, sólo puede funcionar correctamente con el
         variante, Producto B1. Sin embargo, acepta cualquier instancia de
         AbstractProductB como argumento.
        """
        result = collaborator.useful_function_b()
        return f"The result of the A1 collaborating with the ({result})"
    '''
class ConcreteProductA2(AbstractProductA):
    def moda(self,datos) -> str:
        return "La moda es: " + str(datos.mode())
    '''
    def another_useful_function_a(self, collaborator: AbstractProductB) -> str:
        """
        La variante, Producto A2, sólo puede funcionar correctamente con el
         variante, Producto B2. Sin embargo, acepta cualquier instancia de
         AbstractProductB como argumento.
        """
        result = collaborator.useful_function_b()
        return f"The result of the A2 collaborating with the ({result})"
    '''
    
class ConcreteProductA3(AbstractProductA):
    def mediana(self,datos) -> str:
        return "La mediana es: " + str(datos.median())
    '''
    def another_useful_function_a(self, collaborator: AbstractProductB) -> str:
        """
        La variante, Producto A2, sólo puede funcionar correctamente con el
         variante, Producto B2. Sin embargo, acepta cualquier instancia de
         AbstractProductB como argumento.
        """
        result = collaborator.useful_function_b()
        return f"The result of the A2 collaborating with the ({result})"
    '''
'''
Tengo dudas de si deberia meter los 3 calculos en solo 1 abstract
luego pruebar si no ejecuta asi 
'''


class AbstractProductB(ABC):
    """
    Aquí está la interfaz base de otro producto. Todos los productos pueden interactuar
     entre sí, pero la interacción adecuada sólo es posible entre productos de
     la misma variante concreta.
    """
    @abstractmethod
    def grafico_barras(self):
        """
        El Producto B es capaz de hacer lo suyo...
        """
        pass
    '''
    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...pero también puede colaborar con el ProductoA.

         The Abstract Factory se asegura de que todos los productos que crea sean de la
         misma variante y por tanto, compatible.
        """
        pass
        '''
    @abstractmethod
    def histograma(self):
        """
        El Producto B es capaz de hacer lo suyo...
        """
        pass

"""
Los productos de hormigón son creados por las correspondientes fábricas de hormigón.
"""


class ConcreteProductB1(AbstractProductB):
    def grafico_barras(self,datos):
        
        #hazme un grafico de barras con plt
        plt.figure(figsize=(10,5))
        plt.bar(datos)
        plt.show()

    """
    La variante, Producto B1, solo puede funcionar correctamente con la variante,
     Producto A1. Sin embargo, acepta cualquier instancia de AbstractProductA como
     argumento.
    """
    '''
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"
    '''

class ConcreteProductB2(AbstractProductB):
    def histograma(self,datos):
        #hazme un histograma con plt
        plt.figure(figsize=(10,5))
        plt.hist(datos)
        plt.show()
    
    """
    def another_useful_function_b(self, collaborator: AbstractProductA):
        
        La variante, Producto B2, sólo puede funcionar correctamente con el
         variante, Producto A2. Sin embargo, acepta cualquier instancia de
         AbstractProductA como argumento.
        
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"
    """



def client_code(factory: AbstractFactory, datos) -> None:
    """
    El código de cliente funciona con fábricas y productos solo a través de resumen.
     tipos: AbstractFactory y AbstractProduct. Esto te permite pasar por cualquier fábrica.
     o subclase de producto al código del cliente sin romperlo.
    """
    
    datos=pd.read_csv("Ejercicio1/datoslimpios.csv", sep=';', encoding='ISO-8859-1')
    
    
    #aqui llamo a los metodos que busco
    analisis = factory.analisis_estadistico()
    visualizaciones = factory.visualizaciones_graficas()

    

    print(analisis.media(datos['LONGITUD']))
    print(analisis.moda(datos['LONGITUD']))
    print(analisis.mediana(datos['LONGITUD']))
    
    print(visualizaciones.histograma(datos))
    print(visualizaciones.grafico_barras(datos))


if __name__ == "__main__":
    """
    El código del cliente puede funcionar con cualquier clase de fábrica concreta.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("ffff\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())