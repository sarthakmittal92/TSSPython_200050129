import pygame as pg

class Snake:
  # Snake Initialisation
  def __init__(self):
    self.snakeHead = [150, 100] # head position
    self.snakeBody = [[150, 100],[140,100],[130, 100]] # body coordinates
    self.bodyColor = (250,250,250) # body color
    self.headDir = 'R' # head direction
    self.newDir = 'R' # new direction
  # Move Head
  def moveHead (self):
  # move head in desired direction
    if self.headDir == 'R':
      self.snakeHead[0] += 10
    elif self.headDir == 'L':
      self.snakeHead[0] -= 10
    elif self.headDir == 'U':
      self.snakeHead[1] -= 10
    else:
      self.snakeHead[1] += 10
  # Update Snake
  def updateSnake (self, Display, Food, Score):
    # check snake bounds
    if (self.snakeHead in self.snakeBody[1:]) or self.snakeHead[0] < 5 or self.snakeHead[0] > (Display.window[0] - 5) or self.snakeHead[1] < 5 or self.snakeHead[1] > (Display.window[1] - 5):
      Display.gameOver(Score)
    else:
      # check if food was eaten
      if self.snakeHead == Food.foodPos:
        Score.prevScore = Score.score
        Score.score += 1 # score update
        Food.spawnFood = True
      else:
        # move whole body of snake
        tail = self.snakeBody.pop() # removing last bit from body
        tailBox = pg.Rect(tail[0], tail[1], 10, 10)
        pg.draw.rect(Display.gameWindow, Display.bgColor, tailBox) # removing tail from view
      self.moveHead() # moving ahead
      self.snakeBody.insert(0,self.snakeHead.copy()) # adding new head to body
    # draw body as per data
    for bodyPos in self.snakeBody:
      bodyBox = pg.Rect(bodyPos[0], bodyPos[1], 10, 10)
      pg.draw.rect(Display.gameWindow, self.bodyColor, bodyBox)
    # draw head in new position
    headBox = pg.Rect(self.snakeHead[0], self.snakeHead[1], 10, 10)
    pg.draw.rect(Display.gameWindow, self.bodyColor, headBox)