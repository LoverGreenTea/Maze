import pygame
import time

pygame.init()
window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("background.jpg"), [700, 500])

class Player:
    def __init__(self, speed, width, height, x, y, skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
    def draw(self, window):
        window.blit(self.texture, self.hitbox)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.hitbox.x += self.speed
        if keys[pygame.K_LEFT]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed
        if keys[pygame.K_UP]:
            self.hitbox.y -= self.speed
class Wall:
    def __init__(self, width, height, x, y, color):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.color = color



    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

class Gold:
    def __init__(self, width, height, x, y, skin):
        self.texture = pygame.image.load(skin)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

def win_window(window):
    fps = pygame.time.Clock()
    win_lbl = pygame.font.Font(None, 60).render("ти переміг!", True, [0, 0, 0])
    while True:
        window.fill[50, 50, 50]
        window.blit(win_lbl, [200, 200])
        pygame.display.flip()
        fps.tick(60)

player = Player(3, 50, 50, 5, 344, "hero.png")

gold = Gold( 50, 50, 640, 100, "treasure.png")

background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, [700, 500])
game = True

walls = [
    Wall(550, 20,80, 70, [123,123, 123] ),
    Wall(20, 250, 80, 90, [123, 123, 123]),
    Wall(20, 390, 160, 160, [123, 123, 123]),
    Wall(550, 20, 80, 400, [123, 123, 123]),
    Wall(70, 20, 240, 160, [123, 123, 123]),
    Wall(20, 110, 240, 160, [123, 123, 123]),
    Wall(20, 80, 240, 340, [123, 123, 123]),
    Wall(70, 20, 240, 340, [123, 123, 123]),
    Wall(70, 20, 240, 250, [123, 123, 123]),
    Wall(20, 260, 530, 160, [123, 123, 123]),
    Wall(20, 250, 450, 90, [123, 123, 123]),
    Wall(20, 90, 290, 90, [123, 123, 123]),
    Wall(20, 250, 610, 90, [123, 123, 123]),
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)

    player.move()

    if player.hitbox.colliderect(gold.hitbox)
            

    window.fill([255, 0, 0])
    window.blit(background, [0, 0])
    gold.draw(window)
    player.draw(window)


    for wall in walls:
        if player.hitbox.colliderect(wall.hitbox):
            player.hitbox.x = 5
            player.hitbox.y = 344

    for wall in walls:
        wall.draw(window)

    pygame.display.flip()
    fps.tick(60)