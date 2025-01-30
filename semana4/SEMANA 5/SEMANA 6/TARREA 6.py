# clase base: auto
import self


class auto:
     def __init__(self, marca, modelo):
         self.marca = marca    # Atributo publico
         self.modelo = modelo # Atributo publico

     def descripcion(self):
        return f"auto de marca {self.marca}, modelo

        def mover(self):
        return "el auto esta en movimiento"


# Clase derivada: coche (hereda de auto)
class coche(auto):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo) # herencia
        self.__num_puertas = num_puertas # atributos privado

    # metodo para acceder al atributo encapsulado
    def get_num_puertas(self):
        return self.__num_puertas

    # metodo sobrescrito (polimorfismo)
    def mover(self):
        return f"El coche{self.marca} esta conduciendo una persona"


# clase derivada: auto (hereda de vehiculo)
    class auto(vehiculo):
        def __init__(self, mara,modelo tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo # atributos publicos especifico derivadas

    # metodo sobrescrito (polimorfismo)
    def mover(self):
        return f"El auto{self.marca}esta siendo prendida"


# instancias y demostraciones
if __name__ == "main__":
    # crear un auto generico
    auto = auto (maraca: "generico", modelo: "2025"
    print(auto.descripcion())
    print(auto.mover())

    #crear un coche
    coche = coche (maraca: "toyota", modelo: "corolla", num_puertas )
    print(coche.descripcion())
    print(f" el coche tiene {coche.get_num_puertas()}puertas".4)










