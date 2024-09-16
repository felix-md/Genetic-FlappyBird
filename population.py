import  config
import player
import math
import operator


class Population:
    def __init__(self, size : int) -> None:
        self.players = []
        self.atpr_score = 0
        self.generation = 1
        self.species = []
        self.size = size
        for i in range(0,self.size):
            self.players.append(player.Player())
        
    def update_live_players(self ) -> None:
        for p in self.players:
            if p.alive:
                p.look()
                p.think()
                
                p.draw(config.window)
                p.update(config.ground)
                
                
    def natural_selection(self) -> None:
        # print("SPECIATE")
        # self.speciate()
        
        print("CALCULATE FITNESS")
        self.calculate_fitness()
        
        # print("KILL EXTINCT")
        # self.kill_extinct()
        
        # print("KILL STUCK")
        # self.kill_stale()
        
        print("SORT BY FITNESS")
        self.sort_by_fitness()
        
        print("CHILDREN FOR NEXT GEN")
        self.next_gen()
        print("_____________________GEN" + str(self.generation) + "_____________________")
        
  
            
    def calculate_fitness(self) -> None:
        for p in self.players:
            p.calculate_fitness()
     
            
            
    def sort_by_fitness(self) -> None:
        self.players.sort(key=operator.attrgetter('fitness'), reverse=True)
     
        
    def next_gen(self) -> None:
        
        #Clone the champion 
        # for s in self.species:
        #     children.append(s.champion.clone())
            
            
        #Fill open player slots with children
        
        children = self.players[::10]
        for i in range(0,10):
            for _ in range(9):
                child = children[i].clone()
                child.brain.mutate()
                children.append(child)
        
        
        print(len(children))
        self.players = []
        for c in children:
            self.players.append(c)
        
        self.generation += 1
                
    #return true is all players are dead
    def extinct(self) -> bool:
        # print(self.players)
        return not (any( p.alive for p in self.players))