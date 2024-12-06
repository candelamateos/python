from PerroGuia import PerroGuia
from Perro import Raza

class PerroPolicía(PerroGuia):

    # Inicializador de la clase PerroPolicía
    def __init__(self, nombre, color, dueño):
        super().__init__(Raza.PASTOR_ALEMAN, nombre, color, dueño)
        self.energia = 200
        
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