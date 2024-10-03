import pygame
import random

#Intializes pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
#Sets the screens width and heiht
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("FLYING FRENZY!")

#################################### CLASSES ##################################
#Class that initializes all the attributes for the bird
class Bird:
    #Constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velY = 0
        self.gravity = 0.8
        
    #Allows the bird to jump
    def jump(self):
        if click:
            self.velY += self.gravity
            self.y += self.velY

    #Draws the bird to the screen
    def draw(self, screen):
        screen.blit(birdImg, (int(self.x), int(self.y))) 

#Class that initializes all the attributes for the pipes
class Pipe:
    #Constructor method
    def __init__(self, x, difficulty):
        self.x = x
        self.bottomY = random.randint(200, 400)
        self.topY = self.bottomY - 410
        self.width = 100
        self.speed = 5
        self.passes = False
        self.coinX = self.x + self.width // 2 - 30
        self.coinY = random.randint(100, 700) // 2
        self.verticalSpeed = 2  
        self.direction = 1
        self.rockX = self.x + self.width // 2 - 15
        self.rockY = random.randint(self.topY + 30, self.bottomY - 30)
        self.brickX = self.x + self.width + 3
        self.brickY = self.topY + pipeTopImg.get_height() - 20
        self.bricks = []
        self.difficulty = difficulty
        
    #Allows the pipes to move horizontally
    def move(self):
        self.x -= self.speed
        
        if self.difficulty == "easy" or self.difficulty == "medium":
            self.coinX = self.x + self.width // 2 - 30
        
        #Allows the pipes to move vertically
        if self.difficulty == "hard" or self.difficulty == "medium":
            self.bottomY += self.verticalSpeed * self.direction
            self.topY += self.verticalSpeed * self.direction
            self.rockX = self.x + self.width // 2 - 15

            if self.topY <= -125:
                self.direction = 1
            elif self.bottomY >= 375:
                self.direction = -1
                
        #Allows the bricks to move vertically
        if self.difficulty == "hard":
            self.brickY += self.verticalSpeed * self.direction
            self.brickX = self.x + self.width + 3

    #Draws the pipes to the screen
    def draw(self, screen):
        screen.blit(pipeBottomImg, (self.x, self.bottomY))
        screen.blit(pipeTopImg, (self.x, self.topY))
        
        #Draws the bricks to the screen
        if self.difficulty == "hard":
            gapHeight = self.bottomY - self.topY
            brickCount = gapHeight // 65
            
            self.bricks = []

            for i in range(brickCount):
                self.bricks.append((self.brickX, self.brickY + i * 22))
                
            for brick in self.bricks:
                screen.blit(brickImg, brick)
        
        #Draws the coins and rocks to the screen
        if self.difficulty == "medium":
            if pipeCount % 5 == 0:
                screen.blit(coinImg, (self.coinX, self.coinY))
            screen.blit(rockImg, (self.rockX, self.rockY))
        
        if self.difficulty == "easy":
            if pipeCount % 2 == 0:
                screen.blit(coinImg, (self.coinX, self.coinY))
                
        if self.difficulty == "hard":
            if pipeCount % 10 == 0:
                screen.blit(rockImg, (self.rockX, self.rockY))
        
    #Removes coin from screen by changing its Y-value
    def removeCoin(self):
        self.coinY = -500
        
    #Removes bricks from screen by changing its Y-value and removing it from its list
    def removeBrick(self, index):
        if self.difficulty == "hard":
            self.brickY = -500
            self.bricks.pop(index)
        
#Class that initializes all the attributes for the projectiles
class Projectile:
    #Constructor method
    def __init__(self, x, y, xSpeed):
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.active = True

    #Allows them to move horizontally
    def move(self):
        self.x += self.xSpeed
        
    #Draws them onto the screen
    def draw(self, screen):
        if self.active:
            screen.blit(projectileImg, (self.x, self.y))

#Class that initializes all the attributes for the heart
class Hearts:
    #Constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #Draws them onto the screen
    def draw(self,screen):
        screen.blit(heartImg, (self.x, self.y))

#Class that initializes all the attributes for the easy button
class EasyButton:
    #Constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 200
        self.h = 55

    #Draws them onto the screen
    def draw(self,screen):
        screen.blit(easyImg, (self.x, self.y))
        
#Class that initializes all the attributes for the medium button
class MediumButton:
    #Constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 200
        self.h = 55

    #Draws them onto the screen
    def draw(self,screen):
        screen.blit(mediumImg, (self.x, self.y))
        
#Class that initializes all the attributes for the hard button
class HardButton:
    #Constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 200
        self.h = 55

    #Draws them onto the screen
    def draw(self,screen):
        screen.blit(hardImg, (self.x, self.y))
        
#Class that initializes all the attributes for the rules button
class RulesButton:
    #Constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 200
        self.h = 55

    #Draws them onto the screen
    def draw(self,screen):
        screen.blit(rulesImg, (self.x, self.y))
        
#Class that initializes all the attributes for the main menu button
class MainMenuButton:
    #Constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 200
        self.h = 55

    #Draws them onto the screen
    def draw(self,screen):
        screen.blit(mainmenuImg, (self.x, self.y))
        
##Class that initializes all the attributes for the main menu 1 button
class MainMenuButton1:
    #Constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 200
        self.h = 55

    #Draws them onto the screen
    def draw(self,screen):
        screen.blit(mainmenuImg, (self.x, self.y))
        
#################################### FUNCTIONS ################################

#Function given for pixelPerfectCollision
def pixelPerfectCollision(playerImg, enemyImg, playerX, playerY, enemyX, enemyY):
    
    """
    This function will return the collision location of two transparent images
    or None if no collision occurs
    """

    playerMask = pygame.mask.from_surface(playerImg)
    enemyMask = pygame.mask.from_surface(enemyImg)
    offset = (int(playerX - enemyX), int(playerY - enemyY))
    poi = enemyMask.overlap(playerMask, offset)
    return poi

#Function that controls the collision between the bird and both the pipes and allows the score to increase by 1
def collision(bird, pipes):
    global score
    for pipe in pipes:
        if bird.x > pipe.x + pipe.width and pipe.passes == False:
            pipe.passes = True
            score += 1
            
    for pipe in pipes:
        collisionPoint = pixelPerfectCollision(birdImg, pipeBottomImg, bird.x, bird.y, pipe.x, pipe.bottomY)
        if collisionPoint is not None:
            return True

    for pipe in pipes:
        collisionPoint = pixelPerfectCollision(birdImg, pipeTopImg, bird.x, bird.y, pipe.x, pipe.topY)
        if collisionPoint is not None:
            return True
            
    return False

#Function that allows the collision between the rocks and the bird
def collision1 (bird, pipes):
    for pipe in pipes:
        collisionPoint = pixelPerfectCollision(birdImg, rockImg, bird.x, bird.y, pipe.rockX, pipe.rockY)
        if collisionPoint is not None:
            display = True
            return True
        
    return False

#Function that allows the collision between the bricks and the bird, bullet and pipes, bullet and rocks and if the bullet hits the bricks, it is removed from the screen       
def collision2 (bird, pipes):
    for pipe in pipes:
        gapHeight = pipe.bottomY - pipe.topY
        brickCount = gapHeight // 65
        for i in range(brickCount):
            collisionPoint = pixelPerfectCollision(birdImg, brickImg, bird.x, bird.y, pipe.brickX, pipe.brickY + i * 22)
            if collisionPoint is not None:
                return True
            
    for pipe in pipes:
        for bullet in projectiles:
            collisionPoint = pixelPerfectCollision(projectileImg, pipeBottomImg, bullet.x, bullet.y, pipe.x, pipe.bottomY)
            if collisionPoint is not None:
                projectiles.remove(bullet)
            
    for pipe in pipes:
        for bullet in projectiles:
            collisionPoint = pixelPerfectCollision(projectileImg, pipeTopImg, bullet.x, bullet.y, pipe.x, pipe.topY)
            if collisionPoint is not None:
                projectiles.remove(bullet)
            
    for pipe in pipes:
        for bullet in projectiles:
            collisionPoint = pixelPerfectCollision(projectileImg, rockImg, bullet.x, bullet.y, pipe.rockX, pipe.rockY)
            if collisionPoint is not None:
                projectiles.remove(bullet)
            
    for pipe in pipes:
        for bullet in projectiles:
            gapHeight = pipe.bottomY - pipe.topY
            brickCount = gapHeight // 65
            for i in range(brickCount):
                collisionPoint = pixelPerfectCollision(projectileImg, brickImg, bullet.x, bullet.y, pipe.brickX, pipe.brickY + i * 22)
                if collisionPoint is not None:
                    projectiles.remove(bullet)
                    pipe.removeBrick(i)
                    
    return False

#Function that controls the bird and coin collision
def collide(bird , pipes):
    global count, birdImg, display, score
    for pipe in pipes:
        if bird.x > pipe.x + pipe.width and not pipe.passes:
            pipe.passes = True
            count += 1
            score += 1
            
    for pipe in pipes:
        collisionPoint = pixelPerfectCollision(birdImg, coinImg, bird.x, bird.y, pipe.coinX, pipe.coinY)
        if collisionPoint is not None:
            display = True
            
    #If the bird touches a coin, the birdImg turns to a rainbowBirdImg and 2 is added to the score
    for pipe in pipes:
        collisionPoint = pixelPerfectCollision(birdImg, coinImg, bird.x, bird.y, pipe.coinX, pipe.coinY)
        if collisionPoint is not None:
            birdImg = rainbowBirdImg
            pipe.removeCoin()
            count = 0
            score += 2

#Function that controls the collision between the top and bottom of the screen
def out(bird):
    if bird.y < -35:
        bird.y = -35
        bird.velY = -35
        return True

    if bird.y > 402:
        bird.y = 402
        bird.velY = 402
        return True

#Function that resets all of the game variables
def resetGame():
    global score, lives, bird, pipes, move, click, text, stopGame, birdImg, count, display, projectiles
    score = 0
    count = 0
    lives -= 1
    bird = Bird(100, 150)
    birdImg = pygame.image.load("bird.png")
    birdImg = pygame.transform.scale(birdImg, (100, 100))
    pipes = []
    projectiles = []
    move = 0
    click = False
    text = False
    stopGame = False
    display = False

#Function for the easy level
def easy():
    global score, lives, bird, pipes, move, click, text, stopGame, birdImg, count, display, projectiles, pipeCount, heart, right, heartX, heartY, pipeDistance, gameState
    pygame.init()
    
    while True:
        
        mouseX, mouseY = pygame.mouse.get_pos()
        done = False

        # ============================== HANDLE EVENTS ========================= #

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
                break

            # INSERT EVENTS HERE

            if stopGame == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.velY = -9
                        click = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:    
                if gameState == "Easy":
                    if mouseX >= mainmenuButton.x and mouseX <= mainmenuButton.x + mainmenuButton.w and mouseY >= mainmenuButton.y and mouseY <= mainmenuButton.y + mainmenuButton.h:
                        gameState = "Menu"
                        return
             
        if done:
            break
        
        # ============================== MOVE STUFF ============================= #
        bird.jump()
    
        # Move pipes
        if stopGame == False:
            for pipe in pipes:
                pipe.move()

        # ============================== COLLISION ============================== #
        if display == False:
            flag = collision(bird, pipes)

        if flag:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
        
        flag1 = out(bird)
        
        if flag1:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
                
        flag2 = collide(bird, pipes)
        
        if flag2:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
        
        move -= 5

        if move <= -WIDTH:
            move = 0

        # Add new pipes
        pipeCount -= 1
        if click:
            if pipeCount <= 0:
                newPipe = Pipe(WIDTH, "easy")
                pipes.append(newPipe)
                pipeCount = pipeDistance

        # ============================== DRAW STUFF ============================= #
        screen.fill((0, 0, 0))

        screen.blit(backgroundImg, (0, 0))

        for pipe in pipes:
            pipe.draw(screen)

        bird.draw(screen)
        
        for i in range(lives):
            heart = Hearts(heartX + (i * 60), heartY)
            heart.draw(screen)

        screen.blit(groundImg, (0 + move, 475))
        screen.blit(groundImg, (800 + move, 475))

        if count == 3:
            birdImg = pygame.image.load("bird.png")
            birdImg = pygame.transform.scale(birdImg, (100, 100))
            display = False
        
        if text:
            screen.blit(gameoverImg, (150, 150))
            mainmenuButton.draw(screen)
            move = 0

        # Draw score
        font = pygame.font.Font("Flappy Bird.ttf", 65)
        scoreText = font.render(str(score), True, (255, 255, 255))
        screen.blit(scoreText, (375, 100))
    
    # ============================== PYGAME STUFF (DO NOT EDIT) ============= #
        pygame.display.flip()
        pygame.time.delay(20)

    pygame.quit()
    
#Function for the medium level
def medium():
    pygame.init()
    global score, lives, bird, pipes, move, click, text, stopGame, birdImg, count, display, projectiles, pipeCount, heart, right, heartX, heartY, pipeDistance, gameState
    
    while True:
        
        mouseX, mouseY = pygame.mouse.get_pos()
        done = False

    # ============================== HANDLE EVENTS ========================= #

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
                break

            # INSERT EVENTS HERE

            if stopGame == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.velY = -9
                        click = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:    
                if gameState == "Medium":
                    if mouseX >= mainmenuButton.x and mouseX <= mainmenuButton.x + mainmenuButton.w and mouseY >= mainmenuButton.y and mouseY <= mainmenuButton.y + mainmenuButton.h:
                        gameState = "Menu"
                        return

        if done:
            break
        
        # ============================== MOVE STUFF ============================= #
        bird.jump()

        # Move pipes
        if stopGame == False:
            for pipe in pipes:
                pipe.move()

        # ============================== COLLISION ============================== #
        if display == False:
            flag = collision(bird, pipes)

        if flag:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
        
        flag1 = out(bird)
        
        if flag1:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
                
        flag2 = collide(bird, pipes)
        
        if flag2:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
                
        if display == False:
            flag3 = collision1(bird, pipes)
        
        if flag3:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
              
        move -= 5

        if move <= -WIDTH:
            move = 0

        # Add new pipes
        pipeCount -= 1
        if click:
            if pipeCount <= 0:
                newPipe = Pipe(WIDTH, "medium")
                pipes.append(newPipe)
                pipeCount = pipeDistance

        # ============================== DRAW STUFF ============================= #
        screen.fill((0, 0, 0))

        screen.blit(backgroundImg, (0, 0))

        for pipe in pipes:
            pipe.draw(screen)

        bird.draw(screen)
        
        for i in range(lives):
            heart = Hearts(heartX + (i * 60), heartY)
            heart.draw(screen)

        screen.blit(groundImg, (0 + move, 475))
        screen.blit(groundImg, (800 + move, 475))
        
        if count == 3:
            birdImg = pygame.image.load("bird.png")
            birdImg = pygame.transform.scale(birdImg, (100, 100))
            display = False

        if text:
            screen.blit(gameoverImg, (150, 150))
            mainmenuButton.draw(screen)
            move = 0

        # Draw score
        font = pygame.font.Font("Flappy Bird.ttf", 65)
        scoreText = font.render(str(score), True, (255, 255, 255))
        screen.blit(scoreText, (375, 100))
        # ============================== PYGAME STUFF (DO NOT EDIT) ============= #
        pygame.display.flip()
        pygame.time.delay(20)

    pygame.quit()
    
#Function for the hard level
def hard():
    global score, lives, bird, pipes, move, click, text, stopGame, birdImg, count, display, projectiles, pipeCount, heart, right, heartX, heartY, pipeDistance, gameState
    pygame.init()
    
    while True:
        
        mouseX, mouseY = pygame.mouse.get_pos()
        done = False

        # ============================== HANDLE EVENTS ========================= #

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
                break

            # INSERT EVENTS HERE

            if stopGame == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.velY = -9
                        click = True
                        
            if stopGame == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        right = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:    
                if gameState == "Hard":
                    if mouseX >= mainmenuButton.x and mouseX <= mainmenuButton.x + mainmenuButton.w and mouseY >= mainmenuButton.y and mouseY <= mainmenuButton.y + mainmenuButton.h:
                        gameState = "Menu"
                        return
                            
     
        if done:
            break
        
        # ============================== MOVE STUFF ============================= #
        bird.jump()

        # Move pipes
        if stopGame == False:
            for pipe in pipes:
                pipe.move()
            
        for bullet in projectiles:
            bullet.move()
            
        # ============================== COLLISION ============================== #
        if display == False:
            flag = collision(bird, pipes)

        if flag:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
        
        flag1 = out(bird)
        
        if flag1:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
                
        flag2 = collide(bird, pipes)
        
        if flag2:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
                
        if display == False:
            flag3 = collision1(bird, pipes)
        
        if flag3:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
                
        if display == False:
            flag4 = collision2(bird, pipes)
        
        if flag4:
            if lives >= 1:
                resetGame()
            elif lives == 0:
                stopGame = True
                text = True
            
        move -= 5

        if move <= -WIDTH:
            move = 0

        # Add new pipes
        pipeCount -= 1
        if click:
            if pipeCount <= 0:
                newPipe = Pipe(WIDTH, "hard")
                pipes.append(newPipe)
                pipeCount = pipeDistance

        # ============================== DRAW STUFF ============================= #
        screen.fill((0, 0, 0))

        screen.blit(backgroundImg, (0, 0))

        for pipe in pipes:
            pipe.draw(screen)

        for bullet in projectiles:
            bullet.draw(screen)

        bird.draw(screen)
        
        for i in range(lives):
            heart = Hearts(heartX + (i * 60), heartY)
            heart.draw(screen)

        screen.blit(groundImg, (0 + move, 475))
        screen.blit(groundImg, (800 + move, 475))
        
        if count == 3:
            birdImg = pygame.image.load("bird.png")
            birdImg = pygame.transform.scale(birdImg, (100, 100))
            display = False
        
        if stopGame == False:
            if click:
                if right:
                    projectiles.append(Projectile(bird.x + 50, bird.y + 50, 20))
                    right = False

        if text:
            screen.blit(gameoverImg, (150, 150))
            mainmenuButton.draw(screen)
            move = 0

        # Draw score
        font = pygame.font.Font("Flappy Bird.ttf", 65)
        scoreText = font.render(str(score), True, (255, 255, 255))
        screen.blit(scoreText, (375, 100))
        
        # ============================== PYGAME STUFF (DO NOT EDIT) ============= #
        pygame.display.flip()
        pygame.time.delay(20)

    pygame.quit()
    
#Function for to bring the user back to the main menu from the rules
def rules():
    global gameState
    if event.type == pygame.MOUSEBUTTONDOWN:
        if gameState == "Rules":
            if mouseX >= mainmenuButton1.x and mouseX <= mainmenuButton1.x + mainmenuButton1.w and mouseY >= mainmenuButton1.y and mouseY <= mainmenuButton1.y + mainmenuButton1.h:
                gameState = "Menu"
                return

#################################### GLOBAL VARIABLES ########################

# Load Images
backgroundImg = pygame.image.load("background.png")
groundImg = pygame.image.load("ground.png")
birdImg = pygame.image.load("bird.png")
rainbowBirdImg = pygame.image.load("rainbowBird.png")
pipeBottomImg = pygame.image.load("pipeBottom.png")
pipeTopImg = pygame.image.load("pipeTop.png")
rockImg = pygame.image.load("rock.png")
coinImg = pygame.image.load("coin.png")
heartImg = pygame.image.load("heart.png")
easyImg = pygame.image.load("Easy.png")
mediumImg = pygame.image.load("Medium.png")
hardImg = pygame.image.load("Hard.png")
rulesImg = pygame.image.load("Rules.png")
titleImg = pygame.image.load("title.png")
rockImg = pygame.image.load("rock.png")
brickImg = pygame.image.load("brick.png")
projectileImg = pygame.image.load("projectile.png")
gameoverImg = pygame.image.load("gameover.png")
mainmenuImg = pygame.image.load("mainmenu.png")
instructionsImg = pygame.image.load("instructions.png")

# Resizing Images
backgroundImg = pygame.transform.scale(backgroundImg, (800, 600))
groundImg = pygame.transform.scale(groundImg, (850, 150))
birdImg = pygame.transform.scale(birdImg, (100, 100))
rainbowBirdImg = pygame.transform.scale(rainbowBirdImg, (75, 75))
pipeBottomImg = pygame.transform.scale(pipeBottomImg, (300, 300))
pipeTopImg = pygame.transform.scale(pipeTopImg, (300, 300))
rockImg = pygame.transform.scale(rockImg, (50, 50))
coinImg = pygame.transform.scale(coinImg, (25, 25))
heartImg = pygame.transform.scale(heartImg, (50, 50))
easyImg = pygame.transform.scale(easyImg, (200, 55))
mediumImg = pygame.transform.scale(mediumImg, (200, 55))
hardImg = pygame.transform.scale(hardImg, (200, 55))
rulesImg = pygame.transform.scale(rulesImg, (200, 55))
titleImg = pygame.transform.scale(titleImg, (600, 175))
rockImg = pygame.transform.scale(rockImg, (30, 30))
brickImg = pygame.transform.scale(brickImg, (92, 40))
projectileImg = pygame.transform.scale(projectileImg, (40, 20))
gameoverImg = pygame.transform.scale(gameoverImg, (500, 200))
mainmenuImg = pygame.transform.scale(mainmenuImg, (200, 55))
instructionsImg = pygame.transform.scale(instructionsImg, (800, 600))

#Objects for the classes
bird = Bird(100, 150)
heart = Hearts(400, 10)
easyButton = EasyButton(290, 240)
mediumButton = MediumButton(290, 330)
hardButton = HardButton(290, 420)
rulesButton = RulesButton(290, 510)
mainmenuButton = MainMenuButton(290, 350)
mainmenuButton1 = MainMenuButton1(590, 537)

#Setting all variables to False
click = False
text = False
stopGame = False
display = False

pipes = []  # List to store pipes
pipeDistance = 60  # Distance between pipes
pipeCount = pipeDistance

#Setting variables equal to zero
score = 0
move = 0
count = 0
lives = 0

hearts = [] # List to store the hearts
heartY = 10

gameState = "Menu"

#Loads background mmusic
pygame.mixer.music.load("bgMusic.mp3")
pygame.mixer.music.play(-1)

#################################### GAME LOOP ################################
while True:
    
    mouseX, mouseY = pygame.mouse.get_pos() #Detects where the mouse is on the screen
    done = False

    # ============================== HANDLE EVENTS ========================= #

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break

        # INSERT EVENTS HERE
        elif event.type == pygame.MOUSEBUTTONDOWN:    
            if gameState == "Menu":
                #If mouse clicks on easy button, it takes the user to the easy level
                if mouseX >= easyButton.x and mouseX <= easyButton.x + easyButton.w and mouseY >= easyButton.y and mouseY <= easyButton.y + easyButton.h:
                    gameState = "Easy"
                    
                #If mouse clicks on medium button, it takes the user to the medium level
                elif mouseX >= mediumButton.x and mouseX <= mediumButton.x + mediumButton.w and mouseY >= mediumButton.y and mouseY <= mediumButton.y + mediumButton.h:
                    gameState = "Medium"
            
                #If mouse clicks on hard button, it takes the user to the hard level
                elif mouseX >= hardButton.x and mouseX <= hardButton.x + hardButton.w and mouseY >= hardButton.y and mouseY <= hardButton.y + hardButton.h:
                    gameState = "Hard"
                    
                #If mouse clicks on rules button, it takes the user rules page
                elif  mouseX >= rulesButton.x and mouseX <= rulesButton.x + rulesButton.w and mouseY >= rulesButton.y and mouseY <= rulesButton.y + rulesButton.h:
                    gameState = "Rules"
                
                #If mouse clicks on main menu button 1, it takes the user back to the main menu from the rules page
                elif mouseX >= mainmenuButton1.x and mouseX <= mainmenuButton1.x + mainmenuButton1.w and mouseY >= mainmenuButton1.y and mouseY <= mainmenuButton1.y + mainmenuButton1.h:
                    gameState = "Menu"
            
    if done:
        break

    # ============================== DRAW STUFF ============================= #
    #Draws the main menu screen
    if gameState == "Menu":
        screen.fill((0, 0, 0))
        backgroundImg = pygame.transform.scale(backgroundImg, (800, 750))
        screen.blit(backgroundImg, (0, 0))
        screen.blit(titleImg, (100, 10))
        easyButton.draw(screen)
        mediumButton.draw(screen)
        hardButton.draw(screen)
        rulesButton.draw(screen)
        resetGame()
        
    #The gameState is equal to the easy level 
    elif gameState == "Easy":
        lives = 3
        heartX = 600
        easy() #Calls the easy level function 
    
    #The gameState is equal to the medium level 
    elif gameState == "Medium":
        lives = 2
        heartX = 675
        medium() #Calls the medium level function 
    
    #The gameState is equal to the hard level 
    elif gameState == "Hard":
        right = False
        projectiles = [] # List to store the projectiles
        heartX = 730
        lives = 1
        hard() #Calls the hard level function 
        
    #The gameState is equal to the rules page
    elif gameState == "Rules":
        screen.blit(instructionsImg, (0, 0))
        mainmenuButton1.draw(screen)
        rules() #Calls the rules function 

    # ============================== PYGAME STUFF (DO NOT EDIT) ============= #
    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()