import  config
import player
import species

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
        
    def speciate(self) -> None:
        for s in self.species:
            s.players = []
            
        for p in self.players:
            add_to_species = False
            for s in self.species:
                if s.similarity(p.brain):
                    s.add_to_species(p)
                    add_to_species = True
                    break
            if not add_to_species:
                self.species.append(species.Species(p))
            
            
    def calculate_fitness(self) -> None:
        for p in self.players:
            p.calculate_fitness()
        # for s in self.species:
        #     s.calculate_average_fitness()
            
    # def kill_extinct(self) -> None:
    #     species_bin = []
    #     for s in self.species :
    #         if len(s.players) == 0:
    #             species_bin.append(s)
                
    #     for s in species_bin:
    #         self.species.remove(s)    
            
    # def kill_stale(self) -> None :
    #     player_bin = []
    #     species_bin = []
    #     for s in self.species:
    #         if s.staleness >=8:
    #             if len(self.species) > len(species_bin) + 1:
    #                 species_bin.append(s)
    #                 for p in s.players:
    #                     player_bin .append(p)
                        
    #             else:
    #                 s.staleness = 0
    #     for p in player_bin:
    #         self.players.remove(p)
    #     for s in species_bin:
    #         self.species.remove(s)
            
            
    def sort_by_fitness(self) -> None:
        self.players.sort(key=operator.attrgetter('fitness'), reverse=True)
        # for s in self.species:
        #     s.sort_players_by_fitness()
        
        # self.species.sort(key=operator.attrgetter('benchmark_fitness'), reverse=True)
        # print("Atpr score: " + str(self.atpr_score))
        # print("Best of this generation: " + str(self.species[0].champion.fitness))
        # if self.species[0].champion.fitness > self.atpr_score:
        #     self.atpr_score = self.species[0].champion.fitness
        #     print("New atpr score: " + str(self.atpr_score))
        
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
        print(self.players)
        self.generation += 1
                
    #return true is all players are dead
    def extinct(self) -> bool:
        # print(self.players)
        return not (any( p.alive for p in self.players))