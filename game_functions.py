import sys
import pygame

def check_events():
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      sys.exit()
 
def update_screen(ai_settings, screen, ship):
  screen.fill(ai_settings.bg_color)
  ship.blitme()

  pygame.display.flip()
