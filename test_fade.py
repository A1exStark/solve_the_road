import pygame

pygame.init()

w, h = 800, 600
canvas = pygame.Surface((w, h))
window = pygame.display.set_mode((w, h))

white = (255, 255, 255)
black = (0, 0, 0)

run = True

pic = pygame.image.load('img/lvl1/car.png').convert_alpha()
rect = pic.get_rect(center=(w/2, h/2))
alpha = 255
direction = 0

font = pygame.font.Font(('fonts/font.otf'), 30)


while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        alpha = 0
        direction = 0
      elif event.key == pygame.K_RIGHT:
        alpha = 255
        direction = 0
      elif event.key == pygame.K_DOWN:
        direction = -1
      elif event.key == pygame.K_UP:
        direction = 1
      elif event.key == pygame.K_RETURN:
        direction = 0

  alpha += direction
  if alpha < 0:
    alpha = 0
  elif alpha > 255:
    alpha = 255
      
  text_surface = font.render(str(alpha), True, white)
  text_rect = text_surface.get_rect()

  pic.set_alpha(alpha)

  canvas.fill(black)
  canvas.blit(pic, rect)
  canvas.blit(text_surface, text_rect)
  window.blit(canvas, (0, 0, 0, 0))
  pygame.display.update()
  
