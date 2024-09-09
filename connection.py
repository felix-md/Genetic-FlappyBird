import  node as Node
import random


class Connection:
    def __init__(self, from_node : Node, to_node : Node, weight : float) :
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
        
        
    def mutate_weight(self) -> None:
        if random.uniform(0, 1) < 0.1:
            self.weight = random.uniform(-1, 1)
        else:
            self.weight += random.gauss(0, 1) / 10
            self.weight = max(min(self.weight, 1), -1)
                
                
    def clone(self, from_node, to_node):
        clone = Connection(from_node, to_node, self.weight)
        return clone
        
    