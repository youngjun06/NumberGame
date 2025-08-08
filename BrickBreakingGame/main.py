import pygame
pygame.init()

# Screen Setting
width, height = 360, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaking Game")
clock = pygame.time.Clock()

# Font
titel_font = pygame.font.Font(None, 45)
menu_font = pygame.font.Font(None, 30)

game_start = False

# Game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_start:
            game_started = True
    
    screen.fill((250, 250, 250))
    
    title_text = titel_font.render("<Brick Breaking Game>", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(width // 2, height // 2 - 100))
    screen.blit(title_text, title_rect)

    menu_text = menu_font.render("Press any key to start", True, (128, 128, 128))
    title_rect = menu_text.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(menu_text, title_rect)

    pygame.display.flip()
    clock.tick(60)
