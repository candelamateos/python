from enum import Enum
from abc import ABC, abstractmethod

#Crear interfaz que define las acciones basicas de todo animal

class Animales(ABC):

    @abstractmethod
    def nacer(self):
        pass

    @abstractmethod
    def crecer(self):
        pass
    
    @abstractmethod
    def morir(self):
        pass

    @abstractmethod
    def comer(self):
        pass
    
    @abstractmethod
    def dormir(self):
        pass

    @abstractmethod
    def atacar(self):
        pass


# Definición de una enumeración para las razas de perros
class Raza(Enum):
    LABRADOR = "labrador"
    PASTOR_ALEMAN = "pastor aleman"
    CHIHUAHUA = "chihuahua"
    HUSKY = "husky"

class Gorila(Animales):
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 400
        self.nacer()
        

    def nacer(self):
        print("El gorila", self.nombre, "ha nacido")
        
    def crecer(self):
        print("El gorila", self.nombre, "ha crecido")
        
    def comer(self):
        print(self.nombre, "está comiendo")
        
    def dormir(self):
        print(self.nombre, "Esta durmiendo")

    def info(self):
        print(self.nombre, self.energia)
    
    def morir(self):
        print(self.nombre, "ha muerto")

    # Método para que el gorila ataque a otro perro
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.energia // 4
            self.energia -= atacado.energia // 2
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan",self.energia)


# Definición de la clase Perro
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

# Definición de la clase PerroGuia que hereda de Perro
class PerroGuia(Perro):
    
    # Inicializador de la clase PerroGuia
    def __init__(self, raza, nombre, color, dueño):
        super().__init__(raza, nombre, color)
        self.__dueño = dueño

    # Método para que el perro guía ladre y avise al dueño
    def ladrar(self, dueño):
        print(self.nombre, "ladra y avisa a", dueño)

    # Método getter para obtener el dueño
    def get_dueño(self):
        return self.__dueño
    
    # Método para mostrar la información del perro guía
    def info(self):
        super().info()
        print("Este perro pertenece a: ", self.__dueño)
        
    # Método para que el perro a otro animal:
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.energia // 4
            self.energia -= atacado.energia // 2
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan",self.energia)
    
# Definición de la clase PerroPolicía que hereda de PerroGuia
class PerroPolicía(PerroGuia):

    # Inicializador de la clase PerroPolicía
    def __init__(self, nombre, color, dueño):
        super().__init__(Raza.PASTOR_ALEMAN, nombre, color, dueño)
        self.energia = 200
        
    # Método para que el perro policía busque drogas
    def BuscarDroga(self):
        print(self.nombre, "busca droga")
        self.energia -= 50
        
    # Método para que el perro policía ataque a otro perro
    def atacar(self, atacado):
        if self.energia > 0:
            atacado.energia -= self.energia
            print(self.nombre, "ataca a", atacado.nombre, "y le quedan",self.energia)
        else:
            print(self.nombre, "ya estaba muerto")
        # Método para mostrar la información del perro policía
        def info(self):
            super().info()

# Definición de la clase Pelea
class Pelea:
    
    # Inicializador de la clase Pelea
    def __init__(self,animal1, animal2):
        self.animal1 = animal1
        self.animal2 = animal2
        
    # Método para simular la pelea entre dos perros
    def pelear(self):
        print("Se van a enfrentar", self.animal1.nombre, "contra" ,self.animal2.nombre)
        while self.animal1.energia>0 and self.animal2.energia>0:
            self.animal1.atacar(self.animal2)
            input("Presione enter para continuar")
            self.animal2.atacar(self.animal1)
            if self.animal1.energia <= 0:
                print(self.animal2.nombre ,"ganó")
            elif self.animal2.energia <= 0:
                print(self.animal1.nombre, "ganó")

# Creación de instancias de Perro y ejecución de métodos
bobby = Perro("labrador", "Bobby", "Negro")
bobby.info()

luis = Perro("pastor aleman", "Luis", "Blanco")
luis.info()

bruno = PerroGuia("husky","Bruno","blanco", "Paco")
bruno.info()

michael = PerroPolicía("Michael", "Negro", "Poli")
michael.info()

lucas = Gorila("Lucas")
lucas.info()

# Creación de instancias de Pelea y ejecución del método pelear
pelea = Pelea(bobby, luis)
pelea.pelear()

pelea2 = Pelea(michael, luis)
pelea2.pelear()

pelea3 = Pelea(luis, bruno)
pelea3.pelear()

pelea4 = Pelea(lucas, michael)
pelea4.pelear()