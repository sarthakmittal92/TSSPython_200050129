import pygame as pg, sys, time as tm, random as rd

# Window
window = (900, 600) # window dimensions
gameName = 'Snake Eater' # title
bgColor = (0,0,0) # background color
scoreLocation = [50, 20] # score board position
scoreFontProps = {'font': None, 'color': (0,250,0), 'size': 20} # font properties

# Snake Initialisation
snakeHead = [150, 100] # head position
snakeBody = [[150, 100],[140,100],[130, 100]] # body coordinates
bodyColor = (250,250,250) # body color
headDir = 'R' # head direction
newDir = 'R' # new direction

# Food & Score Initialisation
foodPos = [600, 450] # food position
foodColor = (250,0,0) # food color
spawnFood = False # spawn food
score = 0 # count points
prevScore = 0 # score before change

# Initialise Window
pg.init() # initiate
pg.display.set_caption(gameName) # title
gameWindow = pg.display.set_mode(window) # main game window
gameWindow.fill(bgColor) # background

# FPS Controller
fpsc = pg.time.Clock() # speed control
frameRate = 25

# Take Input
def checkEvent ():
  for event in pg.event.get():
    if event.type == pg.QUIT:
      sys.exit(0) # game quit
    elif event.type == pg.KEYDOWN:
      assignKeydown(event.key) # key pressed

# Execute Input
def assignKeydown (key):
  global newDir
  # record key input
  if key == pg.K_RIGHT:
    newDir = 'R'
  elif key == pg.K_LEFT:
    newDir = 'L'
  elif key == pg.K_UP:
    newDir = 'U'
  elif key == pg.K_DOWN:
    newDir = 'D'
  updateDir() # direction update

# Check Input Validity
def updateDir ():
  global headDir, newDir
  # compare directions
  if (headDir == 'R' and newDir != 'L') or (headDir == 'L' and newDir != 'R') or (headDir == 'U' and newDir != 'D') or (headDir == 'D' and newDir != 'U'):
    headDir = newDir

# Move Head
def moveHead ():
  global headDir, snakeHead
  # move head in desired direction
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
  global snakeHead, snakeBody, window, foodPos, score, spawnFood, gameWindow, bgColor, prevScore
  # check snake bounds
  if (snakeHead in snakeBody[1:]) or snakeHead[0] < 5 or snakeHead[0] > (window[0] - 5) or snakeHead[1] < 5 or snakeHead[1] > (window[1] - 5):
    gameOver()
  else:
    # check if food was eaten
    if snakeHead == foodPos:
      prevScore = score
      score += 1 # score update
      spawnFood = True
      createFood() # create new food
    else:
      # move whole body of snake
      tail = snakeBody.pop() # removing last bit from body
      tailBox = pg.Rect(tail[0], tail[1], 10, 10)
      pg.draw.rect(gameWindow, bgColor, tailBox) # removing tail from view
    moveHead() # moving ahead
    snakeBody.insert(0,snakeHead.copy()) # adding new head to body
  
# Spawn New Food
def createFood():
  global spawnFood, foodPos, snakeBody, window
  if spawnFood:
    # food should not be on the body
    while foodPos in snakeBody:
      foodPos = [rd.randrange(10,window[0] - 10,10),rd.randrange(10,window[1] - 10,10)]
    spawnFood = False # food created

# Display Score
def showScore(Location, FontProps):
  global score, bgColor, gameWindow
  # erase previous score
  scoreEraser = pg.font.SysFont(FontProps['font'],FontProps['size']).render('Score: ' + str(prevScore), True, bgColor)
  eraserRect = scoreEraser.get_rect()
  eraserRect.centerx = Location[0]
  eraserRect.centery = Location[1]
  gameWindow.blit(scoreEraser, eraserRect)
  # return new score
  scoreImg = pg.font.SysFont(FontProps['font'],FontProps['size']).render('Score: ' + str(score), True, FontProps['color'])
  scoreRect = scoreImg.get_rect()
  scoreRect.centerx = Location[0]
  scoreRect.centery = Location[1]
  return (scoreImg, scoreRect)

# Re-Draw Screen
def updateScreen():
  global snakeBody, gameWindow, bodyColor, snakeHead, foodColor, foodPos, scoreLocation, scoreFontProps
  # update snake
  updateSnake()
  # draw body as per data
  for bodyPos in snakeBody:
    bodyBox = pg.Rect(bodyPos[0], bodyPos[1], 10, 10)
    pg.draw.rect(gameWindow, bodyColor, bodyBox)
  # draw head in new position
  headBox = pg.Rect(snakeHead[0], snakeHead[1], 10, 10)
  pg.draw.rect(gameWindow, bodyColor, headBox)
  # draw food in new position
  apple = pg.Rect(foodPos[0], foodPos[1], 10, 10)
  pg.draw.rect(gameWindow, foodColor, apple)
  # draw score board
  scoreTuple = showScore(scoreLocation, scoreFontProps)
  gameWindow.blit(scoreTuple[0], scoreTuple[1])
  # display everything
  pg.display.flip()

# End Game
def gameOver():
  global window, scoreFontProps
  # erase game board
  boardEraser = pg.Rect(0, 0, window[0], window[1])
  pg.draw.rect(gameWindow, bgColor, boardEraser)
  # print game over message
  gameOverImg = pg.font.SysFont(None, 48).render('GAME OVER', True, (250,250,250))
  gameOverRect = gameOverImg.get_rect()
  gameOverRect.centerx = window[0] // 2
  gameOverRect.centery = window[1] // 2
  gameWindow.blit(gameOverImg, gameOverRect)
  # print final score
  scoreTuple = showScore([window[0] // 2, 400], scoreFontProps)
  gameWindow.blit(scoreTuple[0], scoreTuple[1])
  # display everything
  pg.display.flip()
  # wait and exit
  tm.sleep(3)
  sys.exit(0)

# Main Loop
while True:
  checkEvent()
  updateScreen()
  fpsc.tick(frameRate)