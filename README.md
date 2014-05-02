DWDM-Network-Optimizer
======================

DWDM Network Optimizer With Redundancy links using an heuristic.

The Heuristic works as follows:

1.- Select a pair of nodes and calculate its shortest path using dijkstra.
2.- Delete temporally all links in the previous path and calculate the shortest path again.
3.- Nodes and links in both paths calculated are asign to the final topology. Then refresh its links weight as 0. 
4.- Repeat steps 1, 2 and 3 for all other nodes within the topology.

Note that the final graph depend of pair of nodes which you decide begin the algorithm.

This project uses Dijkstra algorithm implemented in python by David Eppstein, UC Irvine, 4 April 2002. You can visit http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228

For usage please check the example.py file.
