###
import pygame  
import random
import os

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
resolution = [1280, 720]
screen = pygame.display.set_mode(resolution)

font = pygame.font.Font('brfont.otf',30)
font2 = pygame.font.Font('brfont.otf',100)
font3 = pygame.font.Font('brfont.otf',40)

#필살기
y___ = False
time_seting = pygame.time.get_ticks()
otl_x = font3.render('3초 동안 좌절금지!', True, RED)


#점수 레벨 초기화
point = 0
level = 1

big_sound = pygame.mixer.Sound('big.wav')

#게임 타이틀명
pygame.display.set_caption("좌절 금지")

#현재 시간값을 받아 온다.
clock = pygame.time.Clock()

rices = False

#현재 틱값을 받아 온다.
set_time = pygame.time.get_ticks()
img = pygame.image.load('mob.png')
bg = pygame.image.load('bg.png')
rice = pygame.image.load('bob.png')
char = pygame.image.load('char2.png')
char_size = 100
char = pygame.transform.scale(char, (char_size, char_size))
char_x = 0
char_rect = pygame.Rect(char.get_rect())
rice_size = pygame.Rect(rice.get_rect())
rice_size.left = random.randint(50,1000)
rice_size.top = -100
char_rect.top = resolution[1] - char_rect.width
game_clear = font2.render('미션 완료', True, WHITE)
game_clear1 = font2.render('다들 좌절 금지! 화이팅!', True, WHITE)
game_over = font2.render('게임 오버', True, WHITE)
time_over = font2.render('시간 초과', True, WHITE)
game_info = font2.render('좌절 금지', True, WHITE)
game_info1 = font3.render("1. 상단에서 떨어지는 '좌절'을 피하자", True, WHITE)
game_info2 = font3.render('2. 상단에서 떨어지는 주먹밥을 먹자', True, WHITE)
game_info3 = font3.render('3. 주먹밥을 먹어 점수가 100점이 되면 다음 스테이지로', True, WHITE)
game_info4 = font3.render('스페이스를 누르면 바로 게임이 시작 됩니다.', True, WHITE)
game_info6 = font3.render('"D" 키는 숨은 필살기! 남발하지 마세요! 잼없음!', True, GREEN)
game_info5 = font3.render('SPACE 버튼 게임 시작!!', True, RED)
game_clear_rect = pygame.Rect(game_clear.get_rect())
game_clear1_rect = pygame.Rect(game_clear1.get_rect())
create = font.render('제작 : 스파르타 코딩클럽 이민기',True, WHITE)

start_time = pygame.time.get_ticks()

game_info_rect = pygame.Rect(game_info.get_rect())

class gamestart:
	def __init__(self,mobimg):
		self.mob_imgs = ['mob.png','mob2.png','mob3.png','mob4.png','mob5.png','mob6.png','mob7.png','mob8.png','mob9.png']
		self.mobimg = mobimg
		self.img = pygame.image.load(self.mob_imgs[int(self.mobimg)])
		self.img = pygame.transform.scale(self.img, (100, 100))
		self.mob = pygame.Rect(self.img.get_rect())
		self.mob.left = random.randrange(0,1180,100)
		self.mob.top = -100
	def char(self):
		print(str(self.mobimg),self.mobx,self.moby)
	def img_blit(self):
		global game
		global level
		global y___
		global time_seting
		# global set_time
		# Time = pygame.time.get_ticks() - set_time
		if level == 1:
			speed = 5
		elif level == 2:
			speed = 7
		elif level == 3:
			speed = 10
		else:
			speed = 13
		self.mob.top += speed
		if y___:
			self.mob.top = -200
			screen.blit(otl_x, (480,100))
			time_set = pygame.time.get_ticks() - time_seting
			if time_set > 3000:
				time_seting = pygame.time.get_ticks() 
				y___ = False
				print('필살기 끝!')
		if self.mob.colliderect(char_rect):
			screen.blit(game_over, ( (resolution[0] / 2) - (game_clear_rect.width / 2), resolution[1] / 2) )
			pygame.display.update()
			pygame.time.delay(2000)
			game = False
			pygame.quit()
		if self.mob.top > resolution[1]:
			self.mob.top = -100
			self.mob.left = random.randrange(0,1180,100)
			# self.mobimg = random.randint(0,7)
			self.img = pygame.image.load(self.mob_imgs[int(self.mobimg)])
		screen.blit(self.img, self.mob)
		return self.mob.top

			

Monster_1 = gamestart(0)
Monster_2 = gamestart(4)
# Monster_3 = gamestart(2)
# Monster_4 = gamestart(3)
# Monster_5 = gamestart(4)
# Monster_6 = gamestart(5)
# Monster_7 = gamestart(6)
# Monster_8 = gamestart(7)
# Monster_9 = gamestart(8)

game = True
info = True

#게임 설명
while info:
	screen.blit(game_info, (resolution[0] / 2 - (game_info_rect.width / 2), 20))
	screen.blit(game_info1, (100,200))
	screen.blit(game_info2, (100,280))
	screen.blit(game_info3, (100,360))
	screen.blit(game_info4, (100,440))
	screen.blit(game_info6,(100,500))
	screen.blit(game_info5, (400,600))

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game = False
			info = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				# pygame.time.delay(1000)
				info = False





#게임 루프
while game:
	#시간을 받아와서 프레임 설정
	#루프를 60틱으로 돈다는 뜻!
	clock.tick(60)
	screen.blit(bg, (0,0))
	#게임 이벤트 루프
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game = False
			break

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				y___ = True
				print('숨긴 필살기 좌절금지ㅠㅠ')

		
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_LEFT]:
		char_rect.left -= 10
	elif pressed[pygame.K_RIGHT]:
		char_rect.left += 10
	
		
 
	# char_rect.left = char_rect.left + char_x
    
	if char_rect.left < 0:
		char_rect.left = 0
	elif char_rect.left > resolution[0] - char_rect.width:
		char_rect.left = resolution[0] - char_rect.width

	Monster_1.img_blit()
	Monster_2.img_blit()
	# Monster_3.imgblit()
	# Monster_4.imgblit()
	# Monster_5.imgblit()	
	# Monster_6.imgblit()
	# Monster_7.imgblit()	
	# Monster_8.imgblit()
	# Monster_9.imgblit()

	
	pass__time = (pygame.time.get_ticks() - start_time) / 1000
	# print(int(passtime))
	total_time = 100 - pass__time
 
	# time = pygame.time.get_ticks() - set_time
	# if time > 3000:
	# 	set_time = pygame.time.get_ticks()
	# 	char_size += 10
	# char = pygame.transform.scale(char, (char_size, char_size))
	# if char_x > resolution[0] - char_size:
	# 	char_x -= 5
	# else:
	# 	char_x += 5
	
	if total_time < 0:
		screen.blit(time_over, ( (resolution[0] / 2) - (game_clear_rect.width / 2), resolution[1] / 2) )
		pygame.display.update()
		pygame.time.delay(2000)
		game = False
	
	# print('rice:' + str(rice_size))
	# print(char_rect)
 
	rice_size.top += 10
 
	if char_rect.colliderect(rice_size):
		print('밥과 충돌')
		rices = True
		point += 10
		rice_size.left = 10000
		char_size += 10
		char_rect.width += 10
		char_rect.height += 10
		set_time = pygame.time.get_ticks()
		big_sound.play()
		char = pygame.transform.scale(char, (char_size, char_size))
		char_rect.top = resolution[1] - char_size
		time = pygame.time.get_ticks() - set_time
	
	if rice_size.top > resolution[1]:
		time = pygame.time.get_ticks() - set_time
		if time > 3000:
			set_time = pygame.time.get_ticks()
			rices = False
			rice_size.left = random.randint(0,1000)
			rice_size.top = -100
	
	if point >= 100:
		screen.blit(game_clear, ( (resolution[0] / 2) - (game_clear_rect.width / 2), resolution[1] / 2) )
		char_size = 100
		char_rect.width = 100
		char_rect.height = 100
		char_rect.top = resolution[1] - char_size
		char = pygame.transform.scale(char, (char_size, char_size))
		screen.blit(char, char_rect)
		pygame.display.update()
		pygame.time.delay(2000)
		point = 0
		level += 1
		total_time = 100
		start_time = pygame.time.get_ticks()
	elif level > 3:
		point = 0
		screen.blit(game_clear1, ( (resolution[0] / 2) - (game_clear1_rect.width / 2), resolution[1] / 2) )
		pygame.display.update()
		pygame.time.delay(2000)
		game = False

	# if char_rect.height > 400:
	# 	print('게임종료')
	# 	game = False
	
	text = font.render('점수 : '+str(point), True, WHITE)
	level_text = font.render('난이도 : '+str(level), True, WHITE)
	pass_time = font.render('남은 시간 : ' +str(int(total_time)), True, BLACK)
	screen.blit(char, char_rect)
	screen.blit(rice, rice_size)
	screen.blit(pass_time, (550, 20))
	screen.blit(text, (35,30))
	screen.blit(level_text, (35,70))
	screen.blit(create, (830,660))

	pygame.display.update()

print('종료')
pygame.quit()
