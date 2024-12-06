from Animales import Animales

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