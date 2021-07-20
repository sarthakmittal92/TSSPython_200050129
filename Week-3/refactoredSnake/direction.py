import pygame as pg, sys

# Take Input
def checkEvent (Snake):
  for event in pg.event.get():
    if event.type == pg.QUIT:
      sys.exit(0) # game quit
    elif event.type == pg.KEYDOWN:
      assignKeydown(event.key, Snake) # key pressed

# Execute Input
def assignKeydown (key, Snake):
  # record key input
  if key == pg.K_RIGHT:
    Snake.newDir = 'R'
  elif key == pg.K_LEFT:
    Snake.newDir = 'L'
  elif key == pg.K_UP:
    Snake.newDir = 'U'
  elif key == pg.K_DOWN:
    Snake.newDir = 'D'
  updateDir(Snake) # direction update

# Check Input Validity
def updateDir (Snake):
  # compare directions
  if (Snake.headDir == 'R' and Snake.newDir != 'L') or (Snake.headDir == 'L' and Snake.newDir != 'R') or (Snake.headDir == 'U' and Snake.newDir != 'D') or (Snake.headDir == 'D' and Snake.newDir != 'U'):
    Snake.headDir = Snake.newDir