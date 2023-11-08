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

