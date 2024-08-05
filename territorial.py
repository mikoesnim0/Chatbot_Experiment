import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Territorial PVP Battle")

# Player class
class Player:
    def __init__(self, color, x, y):
        self.color = color
        self.rect = pygame.Rect(x, y, 50, 50)
        self.territory = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def expand_territory(self):
        pygame.draw.rect(self.territory, self.color, self.rect.inflate(10, 10))

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

def check_collision(player1, player2):
    return player1.rect.colliderect(player2.rect)

def main():
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    player1 = Player(RED, 100, 100)
    player2 = Player(BLUE, 600, 400)
    players = [player1, player2]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.move(0, -5)
        if keys[pygame.K_s]:
            player1.move(0, 5)
        if keys[pygame.K_a]:
            player1.move(-5, 0)
        if keys[pygame.K_d]:
            player1.move(5, 0)

        if keys[pygame.K_UP]:
            player2.move(0, -5)
        if keys[pygame.K_DOWN]:
            player2.move(0, 5)
        if keys[pygame.K_LEFT]:
            player2.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            player2.move(5, 0)

        # Check for collisions and expand territory
        if check_collision(player1, player2):
            player1.expand_territory()
            player2.expand_territory()

        # Clear the screen
        screen.fill(WHITE)

        # Draw players' territories
        screen.blit(player1.territory, (0, 0))
        screen.blit(player2.territory, (0, 0))

        # Draw players
        player1.draw(screen)
        player2.draw(screen)

        # Check for win condition
        if player1.rect.x < 0 or player1.rect.x > SCREEN_WIDTH - 50 or player1.rect.y < 0 or player1.rect.y > SCREEN_HEIGHT - 50:
            winner_text = font.render("Player 2 Wins!", True, BLACK)
            screen.blit(winner_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False
        
        if player2.rect.x < 0 or player2.rect.x > SCREEN_WIDTH - 50 or player2.rect.y < 0 or player2.rect.y > SCREEN_HEIGHT - 50:
            winner_text = font.render("Player 1 Wins!", True, BLACK)
            screen.blit(winner_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
```