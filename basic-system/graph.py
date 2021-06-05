
class KnowledgeGraph: 
    
    def __init__(self): 
        self.graph = [] 
    
    def addNode(self, node, multiple=False):  
        if multiple: 
            # node should be a list
            self.graph.extend(node) 
        else:
            self.graph.append(node)

