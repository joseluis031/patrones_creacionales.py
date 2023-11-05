from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
#me crea todos pq lo tengo protegido no privado algun self._product

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

    @property
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

    def tipo_de_masa(self) -> None:
        self._product.add("PartA1")

    def salsa_base(self) -> None:
        self._product.add("PartB1")

    def ingredientes_principales(self) -> None:
        self._product.add("PartC1")
        
    def tecnicas_de_coccion(self) -> None:
        self._product.add("PartD1")
    
    def presentacion(self) -> None:
        self._product.add("PartE1")
        
    def maridajes_recomendados(self) -> None:
        self._product.add("PartF1")
        
    def extras(self) -> None:
        self._product.add("PartG1")
        
    
        
    


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
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    El Director sólo es responsable de ejecutar los pasos de construcción en un
     secuencia determinada. Es útil cuando se producen productos de acuerdo con un
     orden o configuración específica. Estrictamente hablando, la clase Directora es
     Opcional, ya que el cliente puede controlar a los constructores directamente.
    """

    def __init__(self) -> None:
        self._builder = None

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

    def build_pizza(self) -> None:
        self.builder.tipo_de_masa()
        self.builder.salsa_base()
        self.builder.ingredientes_principales()
        self.builder.tecnicas_de_coccion()
        self.builder.presentacion()
        self.builder.maridajes_recomendados()
        self.builder.extras()




if __name__ == "__main__":
    """
    El código del cliente crea un objeto constructor, lo pasa al director y luego
     inicia el proceso de construcción. El resultado final se obtiene del
     objeto constructor.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    

    print("\n")

    print("Standard full featured product,pizza completa: ")
    director.build_pizza()
    builder.product_pizza.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.tipo_de_masa()
    builder.salsa_base()
    builder.ingredientes_principales()
    builder.tecnicas_de_coccion()
    builder.presentacion()
    builder.maridajes_recomendados()
    builder.extras()
    
    builder.product_pizza.list_parts()