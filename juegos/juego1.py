import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego básico con Pygame")

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# Clase para el jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO - 60)

    def update(self):
        # Movimiento del jugador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += 5

# Clase para los enemigos
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.velocidad = random.randint(4, 8)

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, ANCHO - self.rect.width)
            self.velocidad = random.randint(4, 8)

# Crear grupos de sprites
todos_los_sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()

# Instanciar al jugador
jugador = Jugador()
todos_los_sprites.add(jugador)

# Crear enemigos
for i in range(10):
    enemigo = Enemigo()
    todos_los_sprites.add(enemigo)
    enemigos.add(enemigo)

# Puntuación
puntuacion = 0

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Actualizar sprites
    todos_los_sprites.update()

    # Verificar colisiones
    if pygame.sprite.spritecollideany(jugador, enemigos):
        print(f"¡Juego terminado! Puntuación final: {puntuacion}")
        ejecutando = False

    # Incrementar la puntuación
    puntuacion += 1

    # Dibujar todo
    pantalla.fill(NEGRO)
    todos_los_sprites.draw(pantalla)

    # Mostrar puntuación
    fuente = pygame.font.SysFont("Arial", 30)
    texto = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    reloj.tick(60)

pygame.quit()
