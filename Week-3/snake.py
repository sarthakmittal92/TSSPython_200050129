import pygame as pg, sys, time, random as rd

# Window
window = (900, 600) # dimensions
gameName = 'Snake Eater' # title
bgColor = (250,250,250)
scoreLocation = [30, 20]
scoreFontProps = {'font': None, 'color': (0,250,0), 'size': 20}

# Snake Initialisation
snakeHead = [150, 100] # head position
snakeBody = [[150, 100],[140,100],[130, 100]] # body coordinates
bodyColor = (0,0,0)
headDir = 'R' # head direction
newDir = 'R' # new direction

# Food & Score Initialisation
foodPos = [0, 0] # apple position
foodColor = (250,0,0)
spawnFood = False # spawn food
score = 0 # count points

# Initialise Window
pg.init() # initiate
pg.display.set_caption(gameName) # title
gameWindow = pg.display.set_mode(window) # main game window
gameWindow.fill(bgColor) # background

# FPS Controller
fpsc = pg.time.Clock() # speed control

# Take Input
def checkEvent ():
  for event in pg.event.get():
    if event.type = pg.QUIT:
      sys.exit(0) # game quit
    elif event.type == pg.KEYDOWN:
      assignKeydown(event.key) # key pressed

# Execute Input
def assignKeydown (key):
  if key == pg.K_RIGHT:
    newDir = 'R'
  elif key == pg.K_LEFT:
    newDir = 'L'
  elif key == pg.K_UP:
    newDir = 'U'
  elif key == pg.K_DOWN:
    newDir = 'D'
  updateDir()

# Check Input Validity
def updateDir ():
  if (headDir == 'R' and newDir != 'L') or (headDir == 'L' and newDir != 'R') or (headDir == 'U' and newDir != 'D') or (headDir == 'D' and newDir != 'U'):
    headDir = newDir

# Move Head
def moveHead ():
  if headDir == 'R':
    snakeHead[0] += 10
  elif headDir == 'L':
    snakeHead[0] -= 10
  elif headDir == 'U':
    snakeHead[1] -= 10
  else:
    snakeHead[1] += 10

# Update Snake
def updateSnake ():
  if snakeHead in snakeBody[1:] or snakeHead[0] < 5 or snakeHead[0] > (window[0] - 5) or snakeHead[1] < 5 or snakeHead[1] > (window[1] - 5):
    gameOver()
  if snakeHead != foodPos:
    snakeBody.pop()
  else:
    score += 1
    spawnFood = True
    createFood()
  moveHead()
  snakeBody.insert(0,snakeHead)
  
# Spawn New Food
def createFood():
  if spawnFood:
    while foodPos in snakeBody:
      foodPos = [rd.randrange(900),rd.randrange(600)]
    spawnFood = False

# Display Score
def showScore(Location, FontProps):
  scoreImg = pg.font.SysFont(FontProps['font'],FontProps['size']).render('Score: ' + str(score), True, FontProps['color'])
  scoreRect = scoreImg.get_rect()
  scoreRect.x = Location[0]
  scoreRect.y = Location[1]
  return (scoreImg, scoreRect)

# Re-Draw Screen
def updateScreen():
  updateSnake()
  for bodyPos in snakeBody:
    bodyBox = pg.Rect(bodyPos[0], bodyPos[1], 10, 10)
    pg.draw.rect(gameWindow, bodyColor, bodyBox)
  headBox = pg.Rect(snakeHead[0], snakeHead[1], 10, 10)
  pg.draw.rect(gameWindow, bodyColor, headBox)
  apple = pg.Rect(foodPos[0], foodPos[1], 5, 5)
  pg.draw.rect(gameWindow, foodColor, apple)
  scoreTuple = showScore(scoreLocation, scoreFontProps)
  gameWindow.blit(scoreTuple[0], scoreTuple[1])
  pg.display.flip()

# End Game
def gameOver():
  gameOverImg = pg.font.SysFont(None, 48).render('GAME OVER', True, (10,10,10))
  gameOverRect = gameOverImg.get_rect()
  gameOverRect.centerx = window[0] / 2
  gameOverRect.centery = window[1] / 2
  scoreTuple = showScore([window[0] / 2, 400], scoreFontProps)
  gameWindow.blit(scoreTuple[0], scoreTuple[1])
  pg.display.flip()
  sleep(3)
  sys.exit(0)

# Main Loop
while True:
  checkEvent()
  updateScreen()
  fpsc.tick(25)