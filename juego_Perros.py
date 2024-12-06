import pygame
from abc import ABC, abstractmethod

# Inicialización de Pygame
pygame.init()

# Configuración básica
ANCHO, ALTO = 800, 600
FPS = 60
pantalla = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Clase base Perro
class Perro(pygame.sprite.Sprite):
    def __init__(self, x, y, ruta_im, energia=100):
        super().__init__()
        self.image = pygame.image.load(ruta_im).convert()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect(center=(x, y))
        self.energia = 100

    def moverse(self, teclas, arriba, abajo, izquierda, derecha):
        if teclas[arriba]:
            self.rect.y -= 5
        if teclas[abajo]:
            self.rect.y += 5
        if teclas[izquierda]:
            self.rect.x -= 5
        if teclas[derecha]:
            self.rect.x += 5

    def recibir_daño(self, cantidad):
        self.energia -= cantidad
        if self.energia <= 0:
            print("El perro ha sido derrotado.")

    def atacar(self, objetivo):
        print("Perro ataca al objetivo.")
        objetivo.recibir_daño(30)

# Clase derivada PerroPolicía
class PerroPolicía(Perro):
    def __init__(self, x, y, ruta):
        super().__init__(x, y, ruta, energia=150)


# Clase derivada PerroGuía
class PerroGuía(Perro):
    def __init__(self, x, y, ruta):
        super().__init__(x, y, ruta, energia=120)


# Grupo de Sprites
todos_los_perros = pygame.sprite.Group()
perro_policia = PerroPolicía(200, 300, "perro.jpg")
perro_guia = PerroGuía(400, 300, "perro.jpg")
todos_los_perros.add(perro_policia, perro_guia)


# Contenedor de acciones
class Pelea:
    def __init__(self, perro1, perro2):
        self.perro1 = perro1
        self.perro2 = perro2

    
print("¡Comienza la pelea entre los perros!")

# Agregar movimiento con teclas
teclas = {pygame.K_LEFT: (-5, 0), pygame.K_RIGHT: (5, 0),
                pygame.K_UP: (0, -5), pygame.K_DOWN: (0, 5)}
        
jugando = True
while jugando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    jugando = False

            # Detectar teclas presionadas
            keys = pygame.key.get_pressed()
            for key, (dx, dy) in teclas.items():
                if keys[key]:
                    perro_policia.moverse(dx, dy)

            pantalla.fill(BLANCO)

            # Actualizar y dibujar sprites
            todos_los_perros.update()
            todos_los_perros.draw(pantalla)

            pygame.display.flip()
            reloj.tick(FPS)
       
pygame.quit()
