# class node:
#     def __init__(self, data):
#         self.data = data
#         self.childNodes = []


class Graph(object):
    def __init__(self, nodes):
        if nodes is None:
            self.nodes = {}
        else:
            self.nodes = nodes
    
    def vertices(self):
        return list(self.nodes.keys())
    
    def addVertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = []
    
    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.nodes:
            self.nodes[vertex1].append(vertex2)
        else:
            self.nodes[vertex1] = vertex2
    
    def generateEdges(self):
        edges = []
        for vertex in self.nodes:
            for neighbour in self.nodes[vertex]:
                if (vertex, neighbour) not in edges:
                    edges.append({vertex, neighbour})
        return edges
    

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


graph = Graph(g1)
    
print("Vertices of graph:")
print(graph.vertices())

print(graph.generateEdges())

