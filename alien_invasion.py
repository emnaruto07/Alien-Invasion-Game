#!/usr/bin/env python3
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invastion")
  ship = Ship(screen)

  while True:
    gf.check_events()
    gf.update_screen(ai_settings, screen, ship)
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
        sys.exit()

    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()

run_game()
