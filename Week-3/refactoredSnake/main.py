import pygame as pg, direction as dirn, snake, food, display, score

# FPS Controller
fpsc = pg.time.Clock() # speed control

# Game Objects
Snake = snake.Snake()
Food = food.Food()
Display = display.Display()
Score = score.Score()

# Initialise Display
Display.initDisplay()

# Main Loop
while True:
  dirn.checkEvent(Snake)
  Display.updateScreen(Snake, Food, Score)
  fpsc.tick(Display.frameRate)