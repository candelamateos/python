from enum import Enum
from Animales import Animales


class Raza(Enum):
    LABRADOR = "labrador"
    PASTOR_ALEMAN = "pastor aleman"
    CHIHUAHUA = "chihuahua"
    HUSKY = "husky"
    
class Perro(Animales):

    # Inicializador de la clase Perro
    def __init__(self, raza, nombre, color):
        self.nombre = nombre
        self.raza = Raza(raza)
        self.color = color

        # Asignación de la energía según la raza
        if self.raza.value == "labrador":
            self.energia = int(70)
        elif self.raza.value == "pastor aleman":
            self.energia = int(100)
        elif self.raza.value == "chihuahua":
            self.energia = int(50)
        else:
            self.energia = int(80)

    #Métodos heredados de la clase abstracta animal

    def nacer(self):
        print("El perro", self.nombre, "ha nacido")
        self.info
        
    def crecer(self):
        print("El perro", self.nombre, "ha crecido")
        
    def morir(self):
        print("El perro", self.nombre, "ha muerto")
        
    def comer(self):
        print(self.nombre, "está comiendo")
        
    def dormir(self):
        print(self.nombre, "Esta durmiendo")
        

    # Método para simular el ladrido del perro
    def ladrar(self):
        print(self.nombre, "dice guau")
        self.energia -= 5
        
    # Método para simular el movimiento del perro
    def moverse(self):
        print(self.nombre, "camina hacia delante")
        self.energia -= 10

    # Método para mostrar la información del perro
    def info(self):
        print(self.nombre, self.raza.value, self.color, self.energia)
        
    # Método para que el perro ataque a otro perro
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.energia // 2
            self.energia -= atacado.energia // 4
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan",self.energia)
    
    # GETTERS
    def get_nombre(self):
        return self.nombre