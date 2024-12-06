import pygame
import sys
from pygame.locals import *
from enum import Enum

class Raza(Enum):
    LABRADOR = "Labrador"
    PASTOR_ALEMAN = "Pastor Alemán"
    CHIHUAHUA = "Chihuahua"

# Clase Perro
class Perro(pygame.sprite.Sprite):
    def __init__(self, raza, nombre, path, position):
        super().__init__()
        self.nombre = nombre
        self.raza = Raza(raza)
        self.energia = 100 if self.raza == Raza.PASTOR_ALEMAN else 70 if self.raza == Raza.LABRADOR else 50
        self.image = pygame.image.load(path)  # Color refers to image file name
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.speed = 5

    def moverse(self, teclas, arriba, abajo, izquierda, derecha):
        if teclas[arriba]:
            self.rect.y -= 5
        if teclas[abajo]:
            self.rect.y += 5
        if teclas[izquierda]:
            self.rect.x -= 5
        if teclas[derecha]:
            self.rect.x += 5
    
    def regenerar_energia(self):
        self.energia += 5
        if self.energia > 100:
            self.energia = 100

class Pelea:

    def __init__(self, perro1, perro2):
        self.perro1 = perro1
        self.perro2 = perro2
        self.last_regen_time = pygame.time.get_ticks()

    def check_collision(self):
        if self.perro1.rect.colliderect(self.perro2.rect):
            self.perro1.energia -= 10
            self.perro2.energia -= 10
            print(f"{self.perro1.nombre} tiene {self.perro1.energia} de energía")
            print(f"{self.perro2.nombre} tiene {self.perro2.energia} de energía")

    def regenerar_energia(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_regen_time >= 5000:  # Cada 5 segundos
            self.perro1.regenerar_energia()
            self.perro2.regenerar_energia()
            print(f"Energía regenerada: {self.perro1.nombre} ({self.perro1.energia}), {self.perro2.nombre} ({self.perro2.energia})")
            self.last_regen_time = current_time

    def check_game_over(self):
        if self.perro1.energia <= 0:
            print(f"{self.perro2.nombre} gana la pelea")
            return True
        if self.perro2.energia <= 0:
            print(f"{self.perro1.nombre} gana la pelea")
            return True
        return False
    

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pelea de Perros")

    clock = pygame.time.Clock()

    # Crear perros
    perro1 = Perro("Labrador", "Bobby", "perro.jpg", (100, 100))
    perro2 = Perro("Pastor Alemán", "Max", "perro.jpg", (400, 300))

    pelea = Pelea(perro1, perro2)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(perro1, perro2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Movimiento de los perros
        perro1.moverse(keys, K_w, K_s, K_a, K_d)  # Perro 1 usa WASD
        perro2.moverse(keys, K_UP, K_DOWN, K_LEFT, K_RIGHT)  # Perro 2 usa flechas

        # Comprobar colisiones
        pelea.check_collision()

        # Regenerar energía
        pelea.regenerar_energia()

        # Comprobar si el juego termina
        if pelea.check_game_over():
            running = False

        # Dibujar en pantalla
        screen.fill((0, 0, 0))  # Fondo negro
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)  # 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()