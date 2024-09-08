import pygame
import random

class Ground:
    ground_level =500
    
    def __init__(self,win_width : int) -> None:
        self.x,self.y = 0,Ground.ground_level
        self.rect = pygame.Rect(self.x,self.y,win_width,5)
        
    def draw(self,win : pygame.surface) -> None:
        pygame.draw.rect(win,(255,255,255),self.rect)
        
        
        
        
        
        
        
class Pipe:
    width : int = 15
    opening : int = 100
    def __init__(self, win_width: int) -> None:
        #position
        self.x = win_width
        self.bottom_height = random.randint(10,300)
        self.top_height = Ground.ground_level - self.bottom_height - Pipe.opening
        
        #bounding box
        self.bottom_rect,self.top_rect = pygame.Rect(0,0,0,0) ,pygame.Rect(0,0,0,0)
        
        #other attributes
        self.passed = False
        self.off_screen = False
        
    def update(self) -> None:
        self.x -=1
        if self.x + Pipe.width <= 50:
            self.passed = True
        if self.x < -Pipe.width:
            self.off_screen = True
    
    def draw(self,win : pygame.surface) -> None:
        self.bottom_rect = pygame.Rect(self.x,Ground.ground_level - self.bottom_height, self.width, self.bottom_height)
        pygame.draw.rect(win, (255,255,255), self.bottom_rect)
        
        self.top_rect = pygame.Rect(self.x,0, self.width, self.top_height)
        pygame.draw.rect(win, (255,255,255), self.top_rect)
        