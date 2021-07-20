import pygame as pg, random as rd

class Food:
  def __init__(self):
    # Food & Score Initialisation
    self.foodPos = [600, 450] # food position
    self.foodColor = (250,0,0) # food color
    self.spawnFood = True # spawn food
  # Spawn New Food
  def createFood(self, Snake, Display):
    if self.spawnFood:
      # food should not be on the body
      while self.foodPos in Snake.snakeBody:
        self.foodPos = [rd.randrange(10,Display.window[0] - 10,10),rd.randrange(10,Display.window[1] - 10,10)]
      # draw food in new position
      apple = pg.Rect(self.foodPos[0] + 2, self.foodPos[1] + 2, 6, 6)
      pg.draw.rect(Display.gameWindow, self.foodColor, apple)
      self.spawnFood = False # food created