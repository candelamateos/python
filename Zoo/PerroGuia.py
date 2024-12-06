from Perro import Perro

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