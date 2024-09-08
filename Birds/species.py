import Birds
import Birds.player
import NeuralNetwork.brain as brain

import operator
import random

class Species:
    def __init__(self, player :  Birds.player) -> None:
        self.players = []
        self.average_fitness = 0
        self.players.append(player)
        self.threshold = 1.2
        self.benchmark_fitness = player.fitness
        self.benchmark_brain = player.brain.clone()
        self.champion = player.clone()
        self.staleness = 0
        
    def add_to_species(self, player : Birds.player) -> None:
        self.players.append(player)
        
    def similarity(self, other_brain : brain) -> float:
        similarity = self.weight_difference(self.benchmark_brain, other_brain) 
        return similarity < self.threshold
    
    @staticmethod
    def weight_difference(brain1 : brain, brain2 : brain) -> float:
        return sum([abs(brain1.connections[i].weight - brain2.connections[i].weight)
                    for i in range(0, len(brain1.connections))])
        
    def sort_players_by_fitness(self) -> None:
        self.players.sort(key=operator.attrgetter('fitness'), reverse=True)
        if self.players[0].fitness > self.benchmark_fitness:
            self.staleness = 0
            self.benchmark_fitness = self.players[0].fitness
            self.champion = self.players[0].clone()
        else:
            self.staleness +=1
        
    def calculate_average_fitness(self) -> None:
        try:
            self.average_fitness =  \
            sum([player.fitness for player in self.players])/ len(self.players)
        except ZeroDivisionError:
            self.average_fitness = 0

        
    def offspring(self) -> Birds.player:
        baby = self.players[random.randint(1,len(self.players)) - 1].clone()
        baby.brain.mutate()
        return baby