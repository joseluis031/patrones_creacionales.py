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
        masa = input("Introduzca el tipo de masa(normal, fina, extrafina o doble): ")
        self._product_pizza.add("masa elegida: {}".format(masa))

    def salsa_base(self) -> None:
        salsa = input("Introduzca la salsa base(tomate, carbonara, barbacoa o pesto): ")
        self._product_pizza.add("salsa base elegida: {}".format(salsa))

    def ingredientes_principales(self) -> None:
        ingredientes = input("Introduzca los ingredientes principales(jamon, queso, bacon, champiñones, pimiento, cebolla, atun, aceitunas, pollo, carne, gambas, anchoas, salami, chorizo, tomate, maiz, piña o rucula): ")
        self._product_pizza.add("ingredientes principales elegidos: {}".format(ingredientes))
        
    def tecnicas_de_coccion(self) -> None:
        coccion = input("Introduzca las tecnicas de coccion(horno, parrilla, sarten o microondas): ")
        self._product_pizza.add("tecnicas de coccion elegidas: {}".format(coccion))
    
    def presentacion(self) -> None:
        present=input("Introduzca la presentacion(cuadrada, redonda, premium, calzone o sorpresa): ")
        self._product_pizza.add("presentacion elegida: {}".format(present))
        
    def maridajes_recomendados(self) -> None:
        maridaje = input("Introduzca los maridajes recomendados(cerveza, vino, refresco o agua): ")
        self._product_pizza.add("maridajes elegidos: {}".format(maridaje))
        
    def extras(self) -> None:
        ext = input("Introduzca los extras(queso doble, doble de ingredientes, doble de salsa, trufa, caviar, bordes de queso): ")
        self._product_pizza.add("extras elegidos: {}".format(ext))
        
    
        
    


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