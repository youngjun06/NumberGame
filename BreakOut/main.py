'''
게임이 시작되면 위에서는 무작위로 블록 생성 한 줄, 바닥 가운데서 공 하나 생성
공을 한번 쏘면 이전 블록은 한칸 내려오고, 상단에 새로운 블록 생성 점수 +1
블록이 끝까지 내려오면 끝
'''

import pygame
import random

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
exit_button = pygame.Rect(width // 2 - 80, height // 2 + 160, 160, 50)
back_button = pygame.Rect(width // 2 - 80, height // 2 + 160, 160, 50)

# Default
screen_state = "start"
running = True
game_start = False
countdown = 3

def ControlGame():
    global screen_state, running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if screen_state == "start":
                if start_button.collidepoint(event.pos):
                    screen_state = "game"
                    

                elif recode_button.collidepoint(event.pos):
                    screen_state = "recode"
                elif exit_button.collidepoint(event.pos):
                    running = False
            elif screen_state == "recode":
                if back_button.collidepoint(event.pos):
                    screen_state = "start"
            # elif screen_state == "game":


def StartScreen():
    screen.fill((250, 250, 250))
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

def GameScreen():
    global game_start, countdown
    screen.fill((250, 250, 250))
    game_text = start_font.render("START", True, (150, 150, 150))
    game_rect = game_text.get_rect(center=(width // 2, height // 2 - 130))
    screen.blit(game_text, game_rect)

'''
    if not game_start:
        pygame.time.get.ticks()

    else :
        screen.fill((250, 250, 250))
'''
def RecodeScreen():
    screen.fill((250, 250, 250))
    recode_text = title_font.render("Recode", True, (0, 0, 0))
    recode_rect = recode_text.get_rect(center=(width // 2, 80))
    screen.blit(recode_text, recode_rect)

    #Back Button
    pygame.draw.ellipse(screen, (50, 50, 50), back_button)
    exit_button_text = any_font.render("Back", True, (255, 255, 255))
    exit_button_rect = exit_button_text.get_rect(center=(exit_button.center))
    screen.blit(exit_button_text, exit_button_rect)


# Game
while running:
    ControlGame()
    if screen_state == "start":
        StartScreen()
    elif screen_state == "game":
        GameScreen()
    elif screen_state == "recode":
        RecodeScreen()
    pygame.display.flip()
    clock.tick(60)
