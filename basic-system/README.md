### Basic System 

**components** 

- nodes
	- create a user / observation
	- allow nodes to point at each other  
- graph 
	- collection of nodes 
- query
	- make a query into graph based on node relationships


**example** 

Creating and querying a "family tree" graph 


Start off by adding family members and their occupations as python dictionaries. Upon creation, nodes will be given a 128-bit unique identifier. 

 
```python 
 
from node import Node 
from graph import KnowledgeGraph
from query import Query

# add family members and a couple occupations 

bob = Node({
    'name': 'bob', 
    'instance of': 'human',
    'cousin to': 'larry', 
    'son of': 'donald', 
    'occupation': 'teacher'
})

larry = Node({
    'name': 'larry',  
    'instance of': 'human',
    'cousin to': 'bob', 
    'son of': 'howard', 
    'occupation': 'plumber'
})

donald = Node({
    'name': 'donald',  
    'instance of': 'human',
    'father to': 'bob', 
    'brother to': 'howard', 
    'occupation': 'retired'
})

howard = Node({
    'name': 'howard',  
    'instance of': 'human',
    'father to': 'larry', 
    'brother to': 'donald', 
    'occupation': 'retired'
})

teacher = Node({
    'name': 'teacher', 
    'instance of': 'occupation', 
    'pay': '$50,000', 
    'pay type': 'salary'
}) 

plumber = Node({
    'name': 'plumber', 
    'instance of': 'occupation', 
    'pay': '$40', 
    'pay type': 'hourly'
})

retired = Node({
    'name': 'retired', 
    'instance of': 'occupation', 
    'pay': '$0', 
    'pay type': None
})

# 2. alter nodes to include references to other nodes 

bob.alter('data', {'cousin to': larry})
bob.alter('data', {'occupation': teacher})
bob.alter('data', {'son of': donald})

larry.alter('data', {'cousin to': bob})
larry.alter('data', {'occupation': plumber})
larry.alter('data', {'son of': howard})

donald.alter('data', {'father to': bob})
donald.alter('data', {'occupation': retired})
donald.alter('data', {'brother to': howard})

howard.alter('data', {'father to': larry})
howard.alter('data', {'occupation': retired})
howard.alter('data', {'brother to': donald}) 

```

Next, add the nodes to the Knowledge Graph 

```python 

kg = KnowledgeGraph()
kg.addNode([bob, larry, donald, howard, teacher, plumber, retired], multiple=True)

```

Finally, make queries into the knowledge graph through the ```query``` module. A RDF triple is represented as a tuple and full queries can be formed through adding tuples to the list. 

```python 
engine = Query(kg)
engine.query([('human', 'occupation', retired), ('human', 'father to', bob)])

```

returns....

```
[{'name': 'donald',
  'instance of': 'human',
  'father to': <__main__.Node at 0x7fe9e1905bb0>,
  'brother to': <__main__.Node at 0x7fe9e1905f10>,
  'occupation': <__main__.Node at 0x7fe9e1905700>}]
```


