import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 7
ENEMY_SPEED = 3

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Setup Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GitHub Nebula Shooter")
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT - 60, 50, 40)
        
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x + 22, y, 5, 10)
        
    def update(self):
        self.rect.y -= BULLET_SPEED

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH-40), -40, 40, 40)
        
    def update(self):
        self.rect.y += ENEMY_SPEED

# Game Variables
player = Player()
bullets = []
enemies = []
score = 0
running = True

# Main Game Loop
while running:
    screen.fill(BLACK)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.rect.x, player.rect.y))

    # Logic
    player.move(keys)
    
    for b in bullets[:]:
        b.update()
        if b.rect.bottom < 0:
            bullets.remove(b)

    if random.randint(1, 50) == 1:
        enemies.append(Enemy())

    for e in enemies[:]:
        e.update()
        # Collision Detection
        if e.rect.colliderect(player.rect):
            print(f"Game Over! Score: {score}")
            running = False
        
        for b in bullets[:]:
            if e.rect.colliderect(b.rect):
                enemies.remove(e)
                bullets.remove(b)
                score += 1
                break

    # Drawing
    player.draw()
    for b in bullets:
        pygame.draw.rect(screen, YELLOW, b.rect)
    for e in enemies:
        pygame.draw.rect(screen, RED, e.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
