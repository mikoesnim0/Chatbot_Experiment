import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CELL_SIZE = 40 # Size of each cell in the grid
ROWS = SCREEN_HEIGHT // CELL_SIZE
COLS = SCREEN_WIDTH // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple PVP Battle")

# Classes and Functions
class Player:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.territories = []
    
    def add_territory(self, x, y):
        self.territories.append((x, y))
    
    def draw(self):
        for territory in self.territories:
            pygame.draw.rect(screen, self.color, (territory[0] * CELL_SIZE, territory[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def init_board():
    board = [["" for _ in range(COLS)] for _ in range(ROWS)]
    for x in range(COLS):
        for y in range(ROWS):
            if random.random() < 0.1:
                board[y][x] = "obstacle"
    return board

def draw_board(board):
    for y in range(ROWS):
        for x in range(COLS):
            if board[y][x] == "obstacle":
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def claim_territory(player, x, y, board):
    if board[y][x] != "obstacle" and (x, y) not in player.territories:
        player.add_territory(x, y)

# Main Game
def main():
    board = init_board()
    player1 = Player(RED, "Player 1")
    player2 = Player(BLUE, "Player 2")
    players = [player1, player2]
    turn = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x = mouse_x // CELL_SIZE
                grid_y = mouse_y // CELL_SIZE
                claim_territory(players[turn], grid_x, grid_y, board)
                turn = (turn + 1) % 2

        screen.fill(WHITE)
        draw_board(board)
        for player in players:
            player.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()