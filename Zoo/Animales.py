from abc import ABC, abstractmethod

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