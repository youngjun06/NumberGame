import pygame
pygame.init()

# Screen setting
width, height = 360, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Break Out")
clock = pygame.time.Clock()

# Font
title_font = pygame.font.SysFont("showcardgothic", 45, False, False)
any_font = pygame.font.SysFont(None, 30, False, False)
start_font = pygame.font.SysFont(None, 100)

# Button
start_button = pygame.Rect(width // 2 - 80, height // 2, 160, 50)
recode_button = pygame.Rect(width // 2 - 80, height // 2 + 80, 160, 50)
exit_button = pygame.Rect(width // 2 -80, height // 2 + 160, 160, 50)

# Game loop
running = True
game_start = False
recode_look = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button.collidepoint(event.pos):
                running = False
            if not game_start and start_button.collidepoint(event.pos):
                game_start  = True
            if not recode_look and recode_button.collidepoint(event.pos):
                recode_look = True
    
    # start
    screen.fill((250, 250, 250))

    # Click recode button
    if recode_look: 
        recode_text = title_font.render("Recode", True, (0, 0, 0))
        recode_rect = recode_text.get_rect(center=(width // 2, 50))
        screen.blit(recode_text, recode_rect)
    
    elif not game_start:
        # Title
        title_text = title_font.render("<Break Out>", True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(width // 2, height // 2 - 180))
        screen.blit(title_text, title_rect)

        # Start button
        pygame.draw.ellipse(screen, (255, 0, 0), start_button)
        start_button_text = any_font.render("Start", True, (255, 255, 255))
        start_button_rect = start_button_text.get_rect(center=(start_button.center))
        screen.blit(start_button_text, start_button_rect)

        # Recode button
        pygame.draw.ellipse(screen, (100, 100, 100), recode_button)
        recode_button_text = any_font.render("Recode", True, (255, 255, 255))
        recode_button_rect = recode_button_text.get_rect(center=(recode_button.center))
        screen.blit(recode_button_text, recode_button_rect)

        # Exit button
        pygame.draw.ellipse(screen, (50, 50, 50), exit_button)
        exit_button_text = any_font.render("Exit", True, (255, 255, 255))
        exit_button_rect = exit_button_text.get_rect(center=(exit_button.center))
        screen.blit(exit_button_text, exit_button_rect)

    # Click start button
    elif game_start: 
        game_text = start_font.render("START", True, (150, 150, 150))
        game_rect = game_text.get_rect(center=(width // 2, height // 2 - 70))
        screen.blit(game_text, game_rect)




    pygame.display.flip()
    clock.tick(60)
