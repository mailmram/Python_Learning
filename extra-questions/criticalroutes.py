
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        visited = {}
        discoveredNodes = {}
        lowTimeNodes = {}
        crticalEdges = [] 
        graph = {}
        for i in range(n):
            graph[i] = []        
        for i in range(len(connections)):
            graph[connections[i][0]].append(connections[i][1])
            graph[connections[i][1]].append(connections[i][0])
        crticalEdges = self.dfsReturn(graph,0,visited, discoveredNodes, lowTimeNodes, 0, crticalEdges,-1)
        return crticalEdges
        
    def dfsReturn(self,graph,vertex, visited, discoveredNodes, lowTimeNodes, timer, crticalEdges,parentNode):
        visited[vertex] = True
        discoveredNodes[vertex] = timer
        lowTimeNodes[vertex] = timer
        for i in graph[vertex]:
            if i == parentNode:
                continue
            if i not in visited:
                timer += 1
                self.dfsReturn(graph,i, visited,discoveredNodes, lowTimeNodes, timer, crticalEdges,vertex)
                lowTimeNodes[vertex] = min(lowTimeNodes[vertex], lowTimeNodes[i])
                if discoveredNodes[vertex] < lowTimeNodes[i]:
                    crticalEdges.append([vertex, i])                  
            else:
                lowTimeNodes[vertex] = min(lowTimeNodes[vertex], discoveredNodes[i])
        return crticalEdges
        
        
        