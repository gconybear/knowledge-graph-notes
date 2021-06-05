
import random 


class Node: 
    
    def __init__(self, data): 
        self.data = data 
        self.uid = random.getrandbits(128)
        self.node = {
            'data': data, 
            'uid': self.uid
        } 
    
    def alter(self, key, val): 
        "alter a nodes data"  
        
        if key != 'data': 
            self.node[key] = val 
        else: 
            # val should be a dict 
            assert type(val) == dict
            self.node['data'].update(val) 
