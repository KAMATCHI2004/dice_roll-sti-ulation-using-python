import pygame
import random
import os

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Roll Simulator")

# Load images from local directory
dice_images = {
    1: pygame.image.load("dice_1.png"),
    2: pygame.image.load("dice_2.png"),
    3: pygame.image.load("dice_3.png"),
    4: pygame.image.load("dice_4.png"),
    5: pygame.image.load("dice_5.png"),
    6: pygame.image.load("dice_6.png")
}

# Resize dice images
dice_images = {key: pygame.transform.scale(img, (100, 100)) for key, img in dice_images.items()}

# Load background image from local directory
bg_image = pygame.image.load("dice_background2.jpg")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Font
font = pygame.font.Font(None, 40)

# Game Variables
player_scores = [0, 0]
rounds = 5
current_round = 1
turn = 0  # 0 for Player 1, 1 for Player 2

def draw_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def roll_dice():
    return random.randint(1, 6)

def game_loop():
    global turn, current_round
    running = True
    player_rolls = [None, None]

    while running:
        screen.blit(bg_image, (0, 0))  # Draw background
        draw_text(f"Round {current_round}/{rounds}", 320, 50, WHITE)
        draw_text(f"Player 1 Score: {player_scores[0]}", 50, 500, RED)
        draw_text(f"Player 2 Score: {player_scores[1]}", 550, 500, BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    roll = roll_dice()
                    player_rolls[turn] = roll
                    if turn == 1:
                        diff = abs(player_rolls[0] - player_rolls[1])
                        player_scores[1 if player_rolls[1] > player_rolls[0] else 0] += diff
                        current_round += 1
                    turn = (turn + 1) % 2
                    
                    if current_round > rounds:
                        running = False

        # Display dice
        if player_rolls[0]:
            screen.blit(dice_images[player_rolls[0]], (200, 250))
        if player_rolls[1]:
            screen.blit(dice_images[player_rolls[1]], (500, 250))
        
        pygame.display.flip()

    # Determine winner
    screen.fill(BLACK)
    if player_scores[0] > player_scores[1]:
        draw_text("Player 1 Wins!", 320, 250, RED)
    elif player_scores[1] > player_scores[0]:
        draw_text("Player 2 Wins!", 320, 250, BLUE)
    else:
        draw_text("It's a Tie!", 350, 250, WHITE)
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()

# Run game
game_loop()
