


#******************package imports********************************

import pygame
import random
from sys import exit
from pygame import mixer


#-------initialising pygame-------# 
pygame.init()



#******************Main Display********************************


SCREEN_WIDTH= 800 # we should create constants module and save all these constant in. 
SCREEN_HIGHT=450
screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
pygame.display.set_caption('My Sanke Game')
screen.fill((255, 255, 255)) # Fill the background with white
clock = pygame.time.Clock() # our animation speed is domentated by how fast we update our frames- in this case we want to keep it constant


#******************Regualer Surface********************************
# creating a test surface

test_surface= pygame.Surface((100,200))

#using the fill method 
test_surface.fill('Red')

# creating another regular surface and using the image load method. 
sky_surface= pygame.image.load('snake/sky.png')

ground_surface= pygame.image.load('snake/ground.png')


#******************Font Surface ********************************


test_font= pygame.font.Font(None, 50) # the none means we are usig the defult font, and the 50 indicates the size 

# this is the test surface
Text_surface= test_font.render('my game',False,'Green')




#******************Spirits********************************

class food(pygame.sprite.Sprite):
   def __init__(self,WIDTH,HIGHT,COLOR):            # constructor
      super().__init__()

    # Create an image of the block, and fill it with a color.
    # This could also be an image loaded from the disk.
      self.image = pygame.Surface([WIDTH, HIGHT])
      self.image.fill(COLOR)
      #self.rect = Rect(leftX, topY, width, height)
      self.rect = self.image.get_rect()


class greenSnake(pygame.sprite.Sprite):
    def __init__(self,x,y): #Constructor. Pass in the attriputes
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Load the image
        self.image = pygame.image.load('snake/Green.png')

        # Set our transparent color
        self.image.set_colorkey((255,255,255))
         # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
class cobraSnake(pygame.sprite.Sprite):
        
    def __init__(self,x,y): #Constructor. Pass in the attriputes
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Load the image
        self.image = pygame.image.load('snake/Cobra.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        

        
def show_score(x,y):
    score= pygame.font.Font(None, 50)
    score = score.render('Score:' + str(score_value),True,(0,0,0))
    screen.blit(score,(x,y))
        
        
X=random.randint(40,200)
Y=random.randint(0,100)
score_value= 50

my_snake1= cobraSnake(50,100)
my_snake2= cobraSnake(200,300)
my_snake3=greenSnake(0,0)

my_food=food(50,50,(255,255,0))
# This is a list of 'sprites.' two snake in the program is
# added to this list.
# The list is managed by a class called 'Group.'

Two_snakes_group= pygame.sprite.Group()
Two_snakes_group.add(my_snake1,my_snake2)

one_snake_group=pygame.sprite.Group()
one_snake_group.add(my_snake3)

food_group=pygame.sprite.Group()
food_group.add(my_food)




#******************Sound Effects********************************

#mixer.music.load('snake/background.wav')
#mixer.music.play(1)



#******************Main Game Loop********************************
VEL=10 # this means the speed of the press
CONDITION= True
while CONDITION:
    screen.fill((0,0,0))
    for event in pygame.event.get():
      if event.type== pygame.QUIT:
        # we are doing the oppiste of pygame.init() 
        pygame.quit()
        # this is important to exit the while infint loop on the spot 
        exit() 


    # all the surfaces blit functions
    
    screen.blit(test_surface,(0,0))
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(test_surface,(300,50))
    one_snake_group.draw(screen)
    

    Two_snakes_group.draw(screen)
    #food_group.draw(screen)


    #---------Event condition------

    userInput=pygame.key.get_pressed()
    if userInput [pygame.K_LEFT]:
        print(' key is pressed to the left')
        my_snake1.rect.x=my_snake1.rect.x-VEL
        keysound = mixer.Sound("snake/laser.wav")
        keysound.play()
    if userInput [pygame.K_RIGHT]:
        print(' key is pressed to the right')
        my_snake1.rect.x=my_snake1.rect.x+VEL
    if userInput [pygame.K_DOWN]:
        print(' key is pressed to the down')
        my_snake1.rect.y=my_snake1.rect.y+VEL
     
    if userInput [pygame.K_UP]:
        print(' Green Snake key is pressed to the up')
        my_snake1.rect.y=my_snake1.rect.y-VEL
    


   #-------score-------#
    show_score(X,Y)
  

    # we need to update the window every time a change happens
    pygame.display.update()
    # here is where we set our clock rates : this means that this while loop should not run over 60 f/s - this is max we dont have to worry about min
    clock.tick(60)
    pygame.time.delay(100)




