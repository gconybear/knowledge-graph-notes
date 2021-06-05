

def try_node_id(d, p): 
    try: 
        r = d.get(p).node['uid']
    except: 
        r = None
    return r

class Query: 
    
    def __init__(self, graph):  
        try:
            self.graph = [x.node['data'] for x in graph.graph] 
        except: 
            self.graph = graph
    
    
    def query(self, triples): 
        
        """
        triples is list of tuples like ('human', 'cousin to', bob_node)
        """ 
        output = self.graph
        for s,p,o in triples: 
            
            output = [x for x in output if (x.get('instance of') == s) and (try_node_id(x,p) == o.node.get('uid'))]
            
        return output
