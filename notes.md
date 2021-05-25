
### General Notes on Knowledge Graphs  

----- 

*Things to learn (more) about* 

- semantic web  
- ontologies / RDF triples 
- property graphs
- updating data in knowledge graphs 
- graph databases



*Enterprise Knowledge Graphs (EKG)*  

--> notes from [this](https://www.youtube.com/watch?v=r3yMSl5NB_Q)

- Hierarchy of EKG needs (bottom to top)
	- infastructure 
		- scalable storage, fault tolerance, data centers, monitoring, alerts, etc 
	- data 
		- high quality primary datasets, well-defined domain schemas 
	- graph 
		- etl and queries, graph data model, mappings 
	- knowledge 
		- ontologies, modality, provenance 
	- logic 
		- inference proofs 


*KG Basics* 

- primary use case: understand data and relationships between data points  
- examples in practice 
	- [google knowledge graph](https://developers.google.com/knowledge-graph) 
	- [pintrest](https://medium.com/@Pinterest_Engineering) using graphs to model user interests on their platform 
	- [youtube](https://medium.com/@brkyataman/knowledge-graph-and-youtube-29d259fd3dc1) using them as part of their rec system to solve cold start problem 
- linguistic stuff 
	- hyponym (narrow entity) / hypernym (braod entity) 
		- "Harry Potter is a book character" 
			- "Harry Potter" --> hyponym 
			- "book character" --> hypernym 
		- hyponym is instance of hypernym 
- plain text --> semantic information 
	- how to we make that mapping? 
		- ML stuff: supervised, unsupervised, rule-based, POS tagging, etc 
	- [Hearst patterns](https://programmerbackpack.com/content/images/2020/08/Python-Knowledge-Graph---Hearst-Patterns.png) 




