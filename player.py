import sys
from tkinter import Place

from components import Pipe
sys.path.append('D:\Projet hors FAC\Flappy Bird\Genetic FlappyBird\Genetic-FlappyBird')

import  brain
import random
import pygame
import  config


class Player:
    def __init__(self) -> None:
        #Bird attributes
        self.x, self.y = 50, 200
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.vel= 0
        self.flap = False
        self.alive = True
        self.lifespan = 0
        
        
        #Ai related attributes
        self.decision = None
        self.vision = [0.5,1,0.5,0.5]
        self.fitness = 0
        self.inputs = 4
        self.brain = brain.Brain(self.inputs)
        self.brain.generate_net()
        
        
        
    #Game related functions
    def draw(self,win : pygame.surface) -> None:
        pygame.draw.rect(win,self.color,self.rect)
        
    def ground_collision(self, ground : config.components.Ground) -> bool:
        return pygame.Rect.colliderect(self.rect,ground.rect)
    
    def sky_collision(self) -> bool:
        return self.rect.y <= 30
    
    def pipe_collision(self) -> bool:
        return any((pygame.Rect.colliderect(self.rect,pipe.top_rect) or
                   pygame.Rect.colliderect(self.rect,pipe.bottom_rect)) 
                   for pipe in config.pipes)
        
    def update(self, ground : config.components.Ground) -> None:
        if not self.ground_collision(ground) and not self.pipe_collision():
            #Gravity
            self.vel += 0.25
            self.rect.y += self.vel
            if self.vel > 5 :
                self.vel = 5
            
            #increment lifespan
            self.lifespan += 1
        else:
            self.alive = False
            self.vel = 0
            self.flap = False
    
    def bird_flap(self) -> None:
        if not self.flap and not self.sky_collision():
            self.vel = -5
            self.flap = True
        if self.vel >=3:
            self.flap = False
    
    @staticmethod
    def closest_pipe() -> config.components.Pipe:
        for pipe in config.pipes:
            if not pipe.passed :
                return pipe
        
    
        
        
        
        
    #Ai related functions
    
    def look(self) -> None:
        if config.pipes:
            
            #Line to top pipe
            self.vision[0] = max(0, self.rect.center[1] - self.closest_pipe().top_rect.bottom) / 500
            
            pygame.draw.line(config.window, self.color, self.rect.center,
                             (self.rect.center[0], config.pipes[0].top_rect.bottom))
            
            #Line to mid pipe
            self.vision[1] = max(0,  self.closest_pipe().x - self.rect.center[0] ) / 500
            
            pygame.draw.line(config.window, self.color, self.rect.center,
                             (config.pipes[0].x, self.rect.center[1]))
            
        
        
            #Line to bottom pipe
            self.vision[2] = max(0, self.closest_pipe().bottom_rect.top - self.rect.center[1]) / 500
            
            pygame.draw.line(config.window, self.color, self.rect.center,
                             (self.rect.center[0], config.pipes[0].bottom_rect.top))
            
            ground_y = config.ground.rect.top
            self.vision[3] = max(0, ground_y - self.rect.bottom) / 500
            
            pygame.draw.line(config.window, self.color, self.rect.bottomleft,
                             (self.rect.bottomleft[0], ground_y))
        
        
        
        
        
    def think(self) -> None:
        self.decision = self.brain.feed_forward(self.vision)
        print(self.decision)
        if self.decision > 0.8:
            self.bird_flap()
            
    def calculate_fitness(self) -> None:
        self.fitness = self.lifespan
        
    def clone(self) -> 'Player':
        
        clone = Player()
        clone.fitness = self.fitness
        clone.brain = self.brain.clone()
        clone.brain.generate_net()
        return clone
        