from dijkstra import Dijkstra
from dijkstra import shortestPath
import copy

class DWDMNetworkOptimizer(object):

    def deleteLinks(self,path,Graph):
        for k in range(len(path)):
            if k+1 < len(path):
                kS  = path[k]
                kSP = path[k+1]
                del Graph[kS][kSP]
                del Graph[kSP][kS]
                 
    def addLinksToFinalGraph(self,path,FinalGraph):
        for k in range(len(path)):
            if k+1 < len(path):
                kS  = path[k]
                kSP = path[k+1]
                if kS in FinalGraph:
                    if not (kSP in FinalGraph[kS]):
                        FinalGraph[kS].insert(len(FinalGraph[kS]),kSP)    
                else:
                    FinalGraph[kS] = [kSP]
                if  kSP in FinalGraph:                
                    if not (kS in FinalGraph[kSP]):
                        FinalGraph[kSP].insert(len(FinalGraph[kSP]),kS)
                else:
                    FinalGraph[kSP]= [kS] 
                       
    def setLinksAsCero(self,links,Graph):
        for k in range(len(links)):
            if k+1 < len(links):
                kS = links[k]
                kSP = links[k+1]
                Graph[kS][kSP] = 0
                Graph[kSP][kS] = 0
                                
    def calculateOptimizedGraph(self,Graph):
        GraphAux= {}
        FinalGraph={}
        for i in range(1,21):
            iString = str(i)
            for j in range(1,21):
                if i != j:
                    GraphAux = copy.copy(Graph)
                    jString = str(j)
                    pathIToJ = shortestPath(Graph,iString,jString)
                    self.deleteLinks(pathIToJ,GraphAux)
                    self.addLinksToFinalGraph(pathIToJ,FinalGraph)
                    pathIToJ2 = shortestPath(GraphAux,iString,jString)
                    self.addLinksToFinalGraph(pathIToJ2,FinalGraph)
                    self.setLinksAsCero(pathIToJ,Graph)
                    self.setLinksAsCero(pathIToJ2,Graph)
        return FinalGraph