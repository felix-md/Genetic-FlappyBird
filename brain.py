import node
import connection
import random

class Brain:
    
    def __init__(self, inputs : int, clone=False) -> None:
        self.connections = []
        self.nodes = []
        self.inputs = inputs
        self.net = []
        self.layers = 2
        
        if not clone:
            #Create input nodes
            for i in range(0, self.inputs):
                self.nodes.append(node.Node(i))
                self.nodes[i].layer = 0
                
            #Create output node
            self.nodes.append(node.Node(4))
            self.nodes[4].layer = 1
            
            #Create connections
            for i in range(0,4):
                self.connections.append(connection.Connection(self.nodes[i],
                                                            self.nodes[4],
                                                            random.uniform(-1,1)))
      
    
    def connect_nodes(self) -> None:
        for i in range(0,len(self.nodes)):
            self.nodes[i].connections = []
            
        for i in range(0,len(self.connections)):
            self.connections[i].from_node.connections.append(self.connections[i])
            
            
    def generate_net(self) -> None:
        self.connect_nodes()
        self.net = []
        for j in range(0, self.layers):
            for i in range(0, len(self.nodes)):
                if self.nodes[i].layer == j:
                    self.net.append(self.nodes[i])
                    
    def feed_forward(self, vision : list) -> float:
        
        for i in range(self.inputs):
          
            self.nodes[i].output_value = vision[i]
        
        
        for i in range(0,len(self.net)):
            self.net[i].activate()
            
        output_value = self.nodes[4].output_value
        
        for i in range(0, len(self.nodes)):
            self.nodes[i].output_value = 0
            
        return output_value
    
    
    def clone(self) ->'Brain':
        clone = Brain(self.inputs, True)
        
        for n in self.nodes :
            clone.nodes.append(n.clone())
            
        for c in self.connections:
            clone.connections.append(c.clone(clone.getNode(c.from_node.id),
                                             clone.getNode(c.to_node.id)))
            
        clone.layers = self.layers
        clone.connect_nodes()
        return clone
    
    def getNode(self, id) -> 'node' :
        for n in self.nodes :
            if n.id == id:
                return n
            
    def mutate(self):
        
        for i in range(0,len(self.connections)):
            self.connections[i].mutate_weight()
    