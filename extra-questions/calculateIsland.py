import queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        visited = {}
        counter = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == "1":
                    visited = self.calculateIslands(i,j,grid,visited, rows, cols)
                    counter += 1
        return counter
                    
                    
                    
    
    def calculateIslands(self,i,j,grid,visited, rows, cols):
        q = queue.Queue()
        q.put((i,j))       
        visited[(i,j)] = True
        neighbours = [(1,0),(-1,0), (0,1),(0,-1)]
        while q.qsize() > 0:
            elm = q.get()
            #print(elm)
            for neighbour in neighbours:
                r = elm[0]+neighbour[0]
                c = elm[1]+neighbour[1]
                if 0 <= r < rows and 0 <= c < cols:
                    if (r,c) not in visited and grid[r][c] == "1":
                        q.put((r,c))
                        visited[(r,c)] = True
                        #print(visited)
        return visited
                                          
            
        