import pygame

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

pygame.init()

dimensiones = [600, 600]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("TABLERO")

juego_terminado = False

reloj = pygame.time.Clock()
ancho = int(dimensiones[0] / 8)
alto = int(dimensiones[1] / 8)
while juego_terminado is False:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True
    pantalla.fill(BLANCO)
    color = 0
    for i in range(0, dimensiones[0], ancho):
        for j in range(0, dimensiones[1], alto):
            if color % 2 == 0:
                pygame.draw.rect(pantalla, NEGRO, [i, j, ancho, alto], 0)
            else:
                pygame.draw.rect(pantalla, BLANCO, [i, j, ancho, alto], 0)
            color += 1
        color += 1
    pygame.display.flip()
    reloj.tick(5)

pygame.quit()