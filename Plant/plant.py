import pygame
import time
from random import randint
pygame.init()
screen=pygame.display.set_mode((1200,600))
running=False
SKY=(102,205,205)
YELLOW=(255,255,204)
FALL=(0,0,0,0)
x=500
run=True
run1=True
d=0   
k=1
k2=1
reset=False
font=pygame.font.SysFont('sans',12)
font1=pygame.font.SysFont('sans',40)
clock = pygame.time.Clock()
#background
background_image=pygame.image.load("wall.png")
background_image=pygame.transform.scale(background_image,(1200,600))
#mask toa do nhan vat
character_image=pygame.image.load("char.png")
character_image=pygame.transform.scale(character_image,(75,105))
mask = pygame.mask.from_surface(character_image)
#mask land
land_image=pygame.image.load("land.jpg") 
land_image=pygame.transform.scale(land_image,(1200,50))
mask_land=pygame.mask.from_surface(land_image)
#toa do vat rac 1 roi
y1=0
trash1_image=pygame.image.load("trash1.png")
trash1_image=pygame.transform.scale(trash1_image,(70,70))
x1=randint(0,1200)
#toa do vat rac 2 roi
y2=0
trash2_image=pygame.image.load("trash2.png")
trash2_image=pygame.transform.scale(trash2_image,(140,70))
x2=randint(0,1200)
#toa do vat thu 3 roi
y3=0
trash3_image=pygame.image.load("trash3.png")
trash3_image=pygame.transform.scale(trash3_image,(70,90))
x3=randint(0,1200)
#toa do vat thu 4 roi
y4=0
trash4_image=pygame.image.load("trash4.png")
trash4_image=pygame.transform.scale(trash4_image,(140,70))
x4=randint(0,1200)
#toa do vat thu 5 roi
y5=0
trash5_image=pygame.image.load("trash5.png")
trash5_image=pygame.transform.scale(trash5_image,(35,105))
x5=randint(0,1200)
#toa do cay 
y6=445
tree_image=pygame.image.load("tree.png")
tree_image=pygame.transform.scale(tree_image,(70,105))
x6=randint(0,1130)
#toa do tao bang tuyet
y8=500
ice_image=pygame.image.load("ice.png")
ice_image=pygame.transform.scale(ice_image,(105,70))
x8=randint(0,1130)
icecount=0
ice=False
icecheck=False
#toa do epx roi
y7=0
epx_image=pygame.image.load("exp.png")
epx_image=pygame.transform.scale(epx_image,(70,70))
x7=randint(0,1130)
#text diem
score=0
BLACK=(0,0,0)
k1=1
epxcheck=False
count=0
start=True
#hinh khoi dau
start_image=pygame.image.load("start.jpg")
start_image=pygame.transform.scale(start_image,(1200,600))
#text khoi dau
#startbutton
startbutton_image=pygame.image.load("startbutton.png")
startbutton_image=pygame.transform.scale(startbutton_image,(400,100))
#exitbutton
exitbutton_image=pygame.image.load("exitbutton.png")
exitbutton_image=pygame.transform.scale(exitbutton_image,(400,100))
#tutorialbutton
tutorialbutton_image=pygame.image.load("tutorialbutton.png")
tutorialbutton_image=pygame.transform.scale(tutorialbutton_image,(400,100))
#story
story_image=pygame.image.load("story.png")
story_image=pygame.transform.scale(story_image,(1200,600))
#tutorial_display
text=False
dis=0
#name
name_image=pygame.image.load("name.png")
name_image=pygame.transform.scale(name_image,(200,200))
#sound
eat = pygame.mixer.Sound('eat.wav')
coll=pygame.mixer.Sound('coll.wav')
while start:
	clock.tick(60)	
	screen.fill(SKY)
	screen.blit(start_image,(0,0))
	screen.blit(name_image,(500,0))
	startbutton=pygame.Rect(400,200,400,100)
	screen.blit(startbutton_image,(400,200))
	exitbutton=pygame.Rect(400,500,400,100)
	screen.blit(exitbutton_image,(400,500))
	tutorialbutton=pygame.Rect(400,350,400,100)
	screen.blit(tutorialbutton_image,(400,350))
	mouse_x,mouse_y=pygame.mouse.get_pos()
	if text==True:
		screen.blit(story_image,(0,0))
		dis+=1
		if (dis==200):text=False
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			start=False
		#click on start button
		if event.type==pygame.MOUSEBUTTONDOWN:
			if (400<mouse_x<800 and 200<mouse_y<300):
				running=True
				start=False
			if (400<mouse_x<800 and 500<mouse_y<600):
				start=False
			if (400<mouse_x<800 and 350<mouse_y<450):
				text=True
				dis=0
	pygame.display.flip()
while running:
	clock.tick(60)
	mask_pos=(x,445)
	screen.fill(SKY)
	screen.blit(background_image,(0,0))
	pygame.draw.rect(screen,YELLOW,(0,550,1200,50))
	screen.blit(character_image,mask_pos)
	screen.blit(land_image,(0,550))
	character=pygame.Rect(x,445,75,105)
	a2=pygame.Rect(0,0,0,0)
	a3=pygame.Rect(0,0,0,0)
	a4=pygame.Rect(0,0,0,0)
	a5=pygame.Rect(0,0,0,0)
	a7=pygame.Rect(0,0,0,0)
	a8=pygame.Rect(0,0,0,0)
	#lam vat thu nhat roi
	if (k==1):
		a1=pygame.Rect(x1,y1,70,70)
		mask_trash1=pygame.mask.from_surface(trash1_image)
		screen.blit(trash1_image,(x1,y1))
		y1+=3*d 
		d=d+0.2 
		if (y1>=605):
		    y1=0
		    d=0
		    x1=randint(0,1200)
		    k=randint(1,5)		
	#lam vat thu hai roi
	if (k==2):
	    a2=pygame.Rect(x2,y2,140,70)
	    mask_trash2=pygame.mask.from_surface(trash2_image)
	    screen.blit(trash2_image,(x2,y2))
	    y2+=3*d
	    d=d+0.2
	    if (y2>=605):
		    y2=0
		    d=0
		    x2=randint(0,1200)
		    k=randint(1,5)
	if (k==3):
		a3=pygame.Rect(x3,y3,70,90)
		mask_trash3=pygame.mask.from_surface(trash3_image)
		screen.blit(trash3_image,(x3,y3))
		y3+=3*d
		d=d+0.2
		if (y3>=605):
		    y3=0
		    d=0
		    x3=randint(0,1200)
		    k=randint(1,5)
	if (k==4):
		a4=pygame.Rect(x4,y4,140,70)
		mask_trash4=pygame.mask.from_surface(trash4_image)
		screen.blit(trash4_image,(x4,y4))
		y4+=3*d
		d=d+0.2
		if (y4>=605):
		    y4=0
		    d=0
		    x4=randint(0,1200)
		    k=randint(1,5)
	if (k==5):
		a5=pygame.Rect(x5,y5,35,105)
		mask_trash5=pygame.mask.from_surface(trash5_image)
		screen.blit(trash5_image,(x5,y5))
		y5+=3*d
		d=d+0.2
		if (y5>=605):
		    y5=0
		    d=0
		    x5=randint(0,1200)
		    k=randint(1,5)
	#tao cay
	a6=pygame.Rect(x6,y6,70,105)
	screen.blit(tree_image,(x6,y6))
	#tao bang
	if (k2==8):
		icecheck=True
		a8=pygame.Rect(x8,y8,105,70)
		screen.blit(ice_image,(x8,y8))
	if(k2!=8 and icecheck==False):
		k2=randint(1,1000)
	#vat pham dac biet epx
	if (k1==1):
		a7=pygame.Rect(x7,y7,70,70)
		screen.blit(epx_image,(x7,y7))
		y7+=3*d
		d=d+0.1
		if(y7>=605):
			y7=0
			d=0
			x7=randint(0,1200)
			k1=randint(1,8)
	if (k1!=1):
		y7+=3*d
		d=d+0.1
		if(y7>=605):
			y7=0
			d=0
			x7=randint(0,1200)
			k1=randint(1,8)
	#cham vao vat
	for trash in [a1,a2,a3,a4,a5]:
		if character.colliderect(trash): 
			pygame.mixer.Sound.play(coll)			
			d=0
			reset=True
			run=False
			run1=False
			gameover=font1.render("GAME OVER - SPACE TO PLAY AGAIN",True,BLACK)
			sumscore=font1.render("YOUR SCORE: " + str(score),True,BLACK)
			sscreen.blit(gameover,(300,300))
			screen.blit(sumscore,(450,200))
	if character.colliderect(a7):
		epxcheck=True
		count=0
		y7=10000
	#cham vao cay
	if character.colliderect(a6):
		pygame.mixer.Sound.play(eat)
		score+=10
		if epxcheck==True: 
			score+=10
			count+=1
		if count==5: epxcheck=False
		x6=randint(0,1130)
	#cham vao bang
	if character.colliderect(a8):
		ice=True
		y8=10000
	if ice==True: 
		d=0
		icecount+=1
		if (icecount==200):
			ice=False
			icecheck=False
			y8=500
			icecount=0
			x8=randint(0,1130)
			k2=randint(1,1000)
	#hien thi diem
	diem=font.render("YOUR SCORE: "+str(score), True, BLACK)
	screen.blit(diem,(10,10))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==pygame.KEYDOWN:
			if (event.key==pygame.K_RIGHT and run==True):
				g=10
				x+=g*5
				g=g+1
				if (x==1200): run=False
				if (x!=1200): 
					run=True
					run1=True
			if (event.key==pygame.K_LEFT and run1==True):
				g=10
				x-=g*5
				g=g+1
				if (x==0): run1=False
				if (x!=0): 
					run1=True
					run=True
			if (event.key==pygame.K_SPACE and reset==True):
				d=0
				x=500
				k=1
				y1=0
				y2=0
				y3=0
				y4=0
				y5=0
				y6=445
				y7=0
				run=True
				run1=True
				reset=False
				score=0
				epxcheck=False
				icecheck=False
				icecount=0
				ice=False
	pygame.display.flip()
pygame.quit()



