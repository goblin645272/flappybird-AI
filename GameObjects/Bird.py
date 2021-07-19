import pygame



class Bird:
    Imgs = [
    pygame.transform.scale(pygame.image.load("D:/project/FlappyBird-AI-main/GameObjects/sprites/bluebird-downflap.png"),(50,40)),
    pygame.transform.scale(pygame.image.load("D:/project/FlappyBird-AI-main/GameObjects/sprites/bluebird-midflap.png"),(50,40)), 
    pygame.transform.scale(pygame.image.load("D:/project/FlappyBird-AI-main/GameObjects/sprites/bluebird-upflap.png"),(50,40)),
    pygame.transform.scale(pygame.image.load("D:/project/FlappyBird-AI-main/GameObjects/sprites/bluebird-downflap.png"),(50,40))
]
    AnimationTime = 5
    def __init__(self, y, x=100):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.Imgs[1]
        self.x = x
        self.y = y
        self.height = self.y
        self.gravity = 0.3
        self.bird_movement = 0
        self.tilt = 0
        self.rect = self.image.get_rect(center=(100, 320))
        self.imgCount = 0 

    def draw(self, window):
        self.imgCount += 1
        if self.imgCount < self.AnimationTime:
            self.image = self.Imgs[0]
        elif self.imgCount < self.AnimationTime*2:
            self.image = self.Imgs[1]
        elif self.imgCount < self.AnimationTime*3:
            self.image = self.Imgs[2]
        elif self.imgCount < self.AnimationTime*4:
            self.image = self.Imgs[1]
        elif self.imgCount < self.AnimationTime*4 + 1:
            self.image = self.Imgs[0]
            self.imgCount = 0

        if self.tilt <= -80:
            self.image = self.Imgs[1]
            self.imgCount = self.AnimationTime*2
        
        rotated_image = pygame.transform.rotate(self.image, self.tilt)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
        window.blit(rotated_image, new_rect)

    def jump(self):
        self.bird_movement = 0
        self.bird_movement -= 9.5

    def move(self):
        self.bird_movement += self.gravity
        self.y += self.bird_movement * 0.6

        if self.bird_movement < 0 :
            if self.tilt < 25:
                self.tilt = 25
        else:
            if self.tilt > -90:
                self.tilt -= 2

    def get_mask(self):
        return pygame.mask.from_surface(self.image)