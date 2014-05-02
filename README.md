DWDM-Network-Optimizer
======================

DWDM Network Links Optimizer links using an heuristic. 
All network can be represented trought a graph, this is a python implementation of an heuristic that is designed 

The Heuristic works as follows:

1.- Select a pair of nodes and calculate its shortest path using dijkstra.

2.- Delete temporally all links in the previous path and calculate the shortest path again.

3.- Nodes and links in both paths calculated are asign to the final topology. Then refresh its links weight as 0. 

4.- Repeat steps 1, 2 and 3 for all other nodes within the topology.

Note that the final graph depends on the pair nodes which you decide to begin the algorithm.

This project uses Dijkstra algorithm implemented in python by David Eppstein, UC Irvine, 4 April 2002. You can visit http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228

For usage please check the example.py file.

A graph is represented by a python dictionary:

exampleGraph = { 
	'1': {'2':15.7,'3':1.5},
	'2': {'1':15.7 ,'3':14.5},
	'3': {'1':1.5,'2':14.5 },
}

Where 1,2 and 3 are nodes and the value in the dictionary is the link weight between two nodes.
