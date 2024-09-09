import pygame
from sys import exit
import config
import  components
import population as pop

pygame.init( )
clock = pygame.time.Clock()
population = pop.Population(100)


def generate_pipes():
    config.pipes.append(components.Pipe(config.win_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
def main():
    
    pipes_spawn_time = 10
    while True:
        quit_game()
        config.window.fill((0,0,0))
        
        #Spawn Ground
        config.ground.draw(config.window)
        
        #Spawn Pipes
        if pipes_spawn_time <=0 :
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -=1
        
        #Update the Pipes and draw them
        for pipe in config.pipes:
            pipe.draw(config.window)
            pipe.update()
            if pipe.off_screen:
                config.pipes.remove(pipe)
                
                
        #Update the population
        if not population.extinct():
            population.update_live_players()
        else:
            
            config.pipes.clear()
            population.natural_selection()
        
        
        
        
        
        
        
        
        #Clock tick and displt update
        clock.tick(240)
        pygame.display.flip()
        
        
        
main()