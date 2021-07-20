import pygame as pg, time as tm, sys

class Display:
  def __init__(self):
    # Window
    self.window = (900, 600) # window dimensions
    self.gameName = 'Snake Eater' # title
    self.bgColor = (0,0,0) # background color
    self.frameRate = 25
  def initDisplay (self):
    # Initialise Window
    pg.init() # initiate
    pg.display.set_caption(self.gameName) # title
    self.gameWindow = pg.display.set_mode(self.window) # main game window
    self.gameWindow.fill(self.bgColor) # background
  # Re-Draw Screen
  def updateScreen(self, Snake, Food, Score):
    # update snake
    Snake.updateSnake(self, Food, Score)
    # create new food
    Food.createFood(Snake, self)
    # draw score board
    Score.showScore(self)
    # display everything
    pg.display.flip()
  # End Game
  def gameOver(self, Score):
    # erase game board
    boardEraser = pg.Rect(0, 0, self.window[0], self.window[1])
    pg.draw.rect(self.gameWindow, self.bgColor, boardEraser)
    # print game over message
    gameOverImg = pg.font.SysFont(None, 48).render('GAME OVER', True, (250,250,250))
    gameOverRect = gameOverImg.get_rect()
    gameOverRect.centerx = self.window[0] // 2
    gameOverRect.centery = self.window[1] // 2
    self.gameWindow.blit(gameOverImg, gameOverRect)
    # print final score
    Score.scoreLocation = [self.window[0] // 2, 400]
    Score.showScore(self)
    # display everything
    pg.display.flip()
    # wait and exit
    tm.sleep(3)
    sys.exit(0)