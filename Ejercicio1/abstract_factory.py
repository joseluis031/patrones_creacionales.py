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
    def analisis_estadistico(self) -> AbstractProductA_analisis:
        pass
    
    #Creo las 2 funciones que me pide el ejercicio en abstract y luego en concrete ire desarrollandolas 1 a 1
    @abstractmethod
    def visualizaciones_graficas(self) -> AbstractProductB_visualizaciones:
        pass
    


class ConcreteFactory1_Analisis(AbstractFactory):
    """
    Las Fábricas de Hormigón producen una familia de productos que pertenecen a un solo
     variante. La fábrica garantiza que los productos resultantes son compatibles. Nota
     que las firmas de los métodos de Concrete Factory devuelven un resumen
     producto, mientras que dentro del método se instancia un producto concreto.
    """

    def analisis_estadistico(self) -> AbstractProductA_analisis:
        return ConcreteMEDIA(), ConcreteMODA(), ConcreteMEDIANA()
    
    def visualizaciones_graficas(self) -> AbstractProductB_visualizaciones:
        return None


class ConcreteFactory2_Visualizaciones(AbstractFactory):
    """
    Cada fábrica de hormigón tiene una variante de producto correspondiente.
    """

    def visualizaciones_graficas(self) -> AbstractProductB_visualizaciones:
        return ConcreteBARRAS(), ConcreteHISTOGRAMA()
    
    def analisis_estadistico(self) -> AbstractProductA_analisis:
        return None
    


class AbstractProductA_analisis(ABC):
    """
    Cada producto distinto de una familia de productos debe tener una interfaz base. Todo
     Las variantes del producto deben implementar esta interfaz.
    """
    '''
    Aqui creo las 3 funciones (dentro del analisis que llevare a cabo en la fabrica 1)
    que me pide el ejercicio en abstract y luego en concrete ire desarrollandolas 1 a 1
    '''
    @abstractmethod
    def calcular(self) -> str:
        pass
    

"""
Los productos de hormigón son creados por las correspondientes fábricas de hormigón.
"""


class ConcreteMEDIA(AbstractProductA_analisis):
    def calcular(self, datos) -> str:
        media = str(datos.mean())
        return ("La longitud media es: {}".format(media))

class ConcreteMODA(AbstractProductA_analisis):
    
    def calcular(self, datos) -> str:
        moda = str(datos.mode())
        return ("La longitud modal es: {}"  .format(moda))

class ConcreteMEDIANA(AbstractProductA_analisis):
    
    def calcular(self, datos) -> str:
        mediana = str(datos.median())
        return ("La mediana en la columna de longitud es es: {}".format(mediana))


'''
Tengo dudas de si deberia meter los 3 calculos en solo 1 concrete y
luego pruebar si no ejecuta asi 
efectivamente no ejecuta asi, asi que lo he juntado en 1 concrete
'''


class AbstractProductB_visualizaciones(ABC):
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


    @abstractmethod
    def histograma(self):
        """
        El Producto B es capaz de hacer lo suyo...
        """
        pass

"""
Los productos de hormigón son creados por las correspondientes fábricas de hormigón.
"""


class ConcreteBARRAS(AbstractProductB_visualizaciones):
    def grafico_barras(self,datos):
        
        #hazme un grafico de barras con plt
        plt.figure(figsize=(10,5))
        plt.bar(datos['LARGA-DURACION'],datos['GRATUITO'])
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
class ConcreteHISTOGRAMA(AbstractProductB_visualizaciones):   
    def histograma(self,datos):
        #hazme un histograma con plt
        plt.figure(figsize=(10,5))
        plt.hist(datos['LARGA-DURACION'])
        plt.show()


        
   



def client_code(factory: AbstractFactory, datos) -> None:
    """
    El código de cliente funciona con fábricas y productos solo a través de resumen.
     tipos: AbstractFactory y AbstractProduct. Esto te permite pasar por cualquier fábrica.
     o subclase de producto al código del cliente sin romperlo.
    """
    
    
    
    #aqui llamo a los metodos que busco
    analisis = factory.analisis_estadistico()
    visualizaciones = factory.visualizaciones_graficas()

    

    print(analisis.calcular(datos['LONGITUD']))
    print(analisis.calcular(datos['LONGITUD']))
    print(analisis.calcular(datos['LONGITUD']))
    
    print(visualizaciones.grafico_barras(datos))
    print(visualizaciones.histograma(datos))



if __name__ == "__main__":
    """
    El código del cliente puede funcionar con cualquier clase de fábrica concreta.
    """
    datos=pd.read_csv("Ejercicio1/datoslimpios.csv", sep=';', encoding='ISO-8859-1')
    print("elige factoria 1(calculos) o 2(graficos)")
    eleccion=int(input())
    
    if eleccion==1:
        print("Client: Testing client code with the first factory type:")
        client_code(ConcreteFactory1_Analisis(),datos)
    
    if eleccion==2:
        print("Client: Testing the same client code with the second factory type:")
        client_code(ConcreteFactory2_Visualizaciones(),datos)
    else:
        pass