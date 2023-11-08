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


    



class ConcreteFactory_numerico(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def crear_relacion_mes_distrito(self) -> Abstractmes_distrito:
        return Concretemes_distrito_numerico()




class ConcreteFactory_grafica(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def crear_relacion_mes_distrito(self) -> Abstractmes_distrito:
        return Concretemes_distrito_grafica()


    


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
        return moda
    
    

class Concretemes_distrito_grafica(Abstractmes_distrito):
    def moda_mes_distrito(self,datos) -> str:
        moda = datos.groupby('Distrito')['Mes'].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
        moda.plot(kind='bar', figsize=(10,5))
        plt.show()
    



'''
class AbstractProductB(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"

class AbstractProductC(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_c(self) -> str:
        pass
    
class ConcreteProductC1(AbstractProductC):
    def useful_function_c(self) -> str:
        return "The result of the product C1."
    
class ConcreteProductC2(AbstractProductC):
    def useful_function_c(self) -> str:
        return "The result of the product C2."
    
class AbstractProductD(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_d(self) -> str:
        pass
    
class ConcreteProductD1(AbstractProductD):
    def useful_function_d(self) -> str:
        return "The result of the product D1."
    
class ConcreteProductD2(AbstractProductD):
    def useful_function_d(self) -> str:
        return "The result of the product D2."
    
'''
def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    datos=pd.read_csv("Ejercicio1.1/datoslimpiosnumericos.csv", sep=';', encoding='ISO-8859-1')
    relacion1 = factory.crear_relacion_mes_distrito()

    

    print(f"{relacion1.moda_mes_distrito(datos)}")
    
 


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    datos=pd.read_csv("Ejercicio1.1/datoslimpiosnumericos.csv", sep=';', encoding='UTF-8')

    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory_numerico())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory_grafica())