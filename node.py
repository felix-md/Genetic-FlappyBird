import math



class Node:
    def __init__(self, id_number :int) -> None:
        self.id = id_number
        self.layer = 0
        self.input_value = 0
        self.output_value= 0
        self.connections = []
        
    def activate(self) -> None:
        
        def sigmoid(x):
            return 1 / (1 + math.exp(-x))
        
        if self.layer == 1:
            # print("before sigmoid: " + str(self.input_value))
            self.output_value = sigmoid(self.input_value)
            # print("after sigmoid: " + str(self.output_value))
            
        for i in range(0, len(self.connections)):
            self.connections[i].to_node.input_value += \
                self.connections[i].weight * self.output_value
        
        
    def clone(self):
        clone = Node(self.id)
        clone.id = self.id
        clone.layer = self.layer
        return clone