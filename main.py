import pygame as pg
import random as rnd


size = 16
w = 30
h = 20
pg.init()
screen = pg.display.set_mode((w*size, h*size))
pg.display.set_caption("Sssnake Game")

i1 = pg.image.load("images/green.png")
i2 = pg.image.load("images/red.png")

class Point:
	x = 0
	y = 0

direction = 0
length = 2

s = [Point() for _ in range(100)]
f = Point()
f.x = 15
f.y = 10

clock = pg.time.Clock()
running = True
while running:
	clock.tick(20)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False	
		elif event.type == pg.KEYDOWN:
			k = event.key
			if k == pg.K_DOWN:
				direction = 0
			elif k == pg.K_LEFT:
				direction = 1
			elif k == pg.K_RIGHT:
				direction = 2
			elif k == pg.K_UP:
				direction = 3

	if f.x == s[0].x and f.y == s[0].y:
		length+=1
		f.x = rnd.randint(0, w-1)
		f.y = rnd.randint(0, h-1)

	if length == 100:
		length = 2

	for i in range(length, 0, -1):
		s[i].x, s[i].y = s[i-1].x, s[i-1].y
			
	if direction == 0:
		s[0].y+=1
	elif direction == 1:
		s[0].x-=1
	elif direction == 2:
		s[0].x+=1
	elif direction == 3:
		s[0].y-=1

	if s[0].x < 0:
		s[0].x = w-1
	elif s[0].x > w-1:
		s[0].x = 0
	if s[0].y < 0:
		s[0].y = h-1
	elif s[0].y > h-1:
		s[0].y = 0
	
	for i in range(1, length):
		if s[0].x == s[i].x and s[0].y == s[i].y:
			length = 2
	
	screen.fill((255, 255, 255))
	
	for i in range(length):
		screen.blit(i1, (s[i].x*size, s[i].y*size))
		screen.blit(i2, (f.x*size, f.y*size))
		
	pg.display.flip()

pg.quit()











