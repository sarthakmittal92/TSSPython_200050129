import pygame as pg

class Score:
  def __init__(self):
    self.score = 0
    self.prevScore = 0
    self.scoreLocation = [50, 20] # score board position
    self.scoreFontProps = {'font': None, 'color': (0,250,0), 'size': 20} # font properties 
  # Display Score
  def showScore(self, Display):
    # erase previous score
    scoreEraser = pg.font.SysFont(self.scoreFontProps['font'], self.scoreFontProps['size']).render('Score: ' + str(self.prevScore), True, Display.bgColor)
    eraserRect = scoreEraser.get_rect()
    eraserRect.centerx = self.scoreLocation[0]
    eraserRect.centery = self.scoreLocation[1]
    Display.gameWindow.blit(scoreEraser, eraserRect)
    # return new score
    scoreImg = pg.font.SysFont(self.scoreFontProps['font'], self.scoreFontProps['size']).render('Score: ' + str(self.score), True, self.scoreFontProps['color'])
    scoreRect = scoreImg.get_rect()
    scoreRect.centerx = self.scoreLocation[0]
    scoreRect.centery = self.scoreLocation[1]
    Display.gameWindow.blit(scoreImg, scoreRect)