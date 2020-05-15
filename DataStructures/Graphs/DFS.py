from queue import *

class Graph(object):

    def __init__(self, nodes):
        if nodes is None:
            self.nodes = {}
        else:
            self.nodes = nodes
    
    def getVertices(self):
        return list(self.nodes.keys())

    def addVertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = []
    
    def addEdges(self, vertex1, vertex2):
        if vertex1 in self.nodes.keys:
            self.nodes[vertex1].append(vertex2)
        else:
            self.nodes[vertex1] = vertex2
    
    def generateEdges(self):
        graphedges = []
        for vertex in self.nodes:
            for neighbours in self.nodes[vertex]:
                graphedges.append((vertex, neighbours))
        return graphedges

    def dfs(self):
        visited = {} 
        for vertex in self.nodes:
            self.dfsReturn(vertex, visited)

    def dfsReturn(self, vertex, visited):
        if vertex not in visited:
            visited[vertex] = True
            print("Node " + str(vertex) + "\n")         
        for i in self.nodes[vertex]:
            if i not in visited:
                self.dfsReturn(i, visited)

    def bfs(self):
        visited = {}
        q = Queue() 
        for vertex in self.nodes:
            visited = self.bfsReturn(vertex, visited, q)

    def bfsReturn(self, vertex, visited, q):
        if vertex not in visited:
            visited[vertex] = True
            q.put(vertex)       
        while q.qsize() > 0:
            s = q.get()
            print("Node " + str(s) + "\n")
            for i in self.nodes[s]:
                if i not in visited:
                    q.put(i)
                    visited[i] = True
        
        return visited
                    

        



g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }
g1 = { 0 : [1,4,5],
          1: [3],
          2 : [1],
          3 : [2, 4],
          4 : [],
          5 : []
        }


graph = Graph(g)
    
print("Vertices of graph:")
print(graph.getVertices())

#print(graph.generateEdges())
graph.bfs()
