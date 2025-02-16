import pygame
import random
import colorsys

# Configurações gerais
WIDTH, HEIGHT = 800, 600
CHAR_SIZE = 30
FIREWORK_SPAWN_TIME = 8

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, CHAR_SIZE)
clock = pygame.time.Clock()


class Letter:
    def __init__(self, char, x, y):
        self.char = char
        self.x = x
        self.y = y
        self.dx = x - font.size(char)[0] // 2
        self.dy = y + CHAR_SIZE // 2

        hue = (x / WIDTH) * 368 % 360
        self.color = self.hsl_to_rgb(hue, 80, 50)
        self.light_color = self.hsl_to_rgb(hue, 88, 70)
        self.alpha_color = self.hsl_to_rgb(hue, 80, 50, alpha=0.5)

        self.reset()

    def reset(self):
        self.phase = "firework"
        self.tick = 8
        self.spawned = False
        self.spawning_time = FIREWORK_SPAWN_TIME * random.random()

    def hsl_to_rgb(self, h, s, l, alpha=255):
        r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
        return (int(r * 255), int(g * 255), int(b * 255), int(alpha))

    def draw(self):
        text_surface = font.render(self.char, True, self.color)
        screen.blit(text_surface, (self.dx, self.dy))


# Exemplo de uso
letters = [Letter(chr(65 + i), random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for i in range(10)]

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for letter in letters:
        letter.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
