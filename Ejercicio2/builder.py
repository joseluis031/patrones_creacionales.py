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
        lista_masa = ["normal", "fina", "extrafina", "doble"]
        masa = input("Introduzca el tipo de masa(normal, fina, extrafina o doble): ")
        if masa not in lista_masa:
            print("no tenemos esa masa, Introduzca un tipo de masa valido")
            self.tipo_de_masa()
        else:
            self._product_pizza.add("masa elegida: {}".format(masa))

    def salsa_base(self) -> None:
        lista_salsa = ["tomate", "carbonara", "barbacoa", "pesto"]
        salsa = input("Introduzca la salsa base(tomate, carbonara, barbacoa o pesto): ")
        if salsa not in lista_salsa:
            print("no tenemos esa salsa, Introduzca una salsa valida")
            self.salsa_base()
        else:
            self._product_pizza.add("salsa base elegida: {}".format(salsa))

    def ingredientes_principales(self) -> None:
        lista_ingredientes = ["jamon", "queso", "bacon", "champinones", "pimiento", "cebolla", "atun", "aceitunas", "pollo", "carne", "gambas", "anchoas", "salami", "chorizo", "tomate", "maiz", "piña", "rucula"]
    
        # Crea una lista para almacenar los ingredientes elegidos
        ingredientes_elegidos = []
        
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
        coccion = input("Introduzca las tecnicas de coccion(horno, parrilla, sarten o microondas): ")
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
        
    def extras(self) -> None:
        lista_extras = ["queso doble", "doble de ingredientes", "doble de salsa", "trufa", "caviar", "bordes de queso"]
    
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
        print(f"El cliente ha elegido su pizza. {', '.join(self.parts)}", end="")


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