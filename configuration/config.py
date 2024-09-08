import sys
sys.path.append('D:\Projet hors FAC\Flappy Bird\Genetic FlappyBird\Genetic-FlappyBird')

import pygame
import configuration.components as components

win_height = 720
win_width = 550
window = pygame.display.set_mode((win_width, win_height))

ground = components.Ground(win_width)
pipes = []