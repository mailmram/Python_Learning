class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        changed = True
        counter = 0
        while changed is True:
            visited = {}
            changed = False
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if (i,j) not in visited and grid[i][j] == 1:
                        visited[(i,j)] = True
                        if i+1 < len(grid) and grid[i+1][j] == 0 and (i+1,j) not in visited:
                            grid[i+1][j] = 1
                            visited[(i+1,j)] = True
                            changed = True
                        if j+1 < len(grid[i]) and grid[i][j+1] == 0 and (i,j+1) not in visited:
                            grid[i][j+1] = 1
                            visited[(i,j+1)] = True
                            changed = True
                        if i-1 >= 0 and grid[i-1][j] == 0 and (i-1,j) not in visited:
                            grid[i-1][j] = 1
                            visited[(i-1,j)] = True
                            changed = True
                        if j-1 >= 0 and grid[i][j-1] == 0 and (i,j-1) not in visited:
                            grid[i][j-1] = 1
                            visited[(i,j-1)] = True
                            changed = True
                    # elif (i,j) not in visited and grid[i][j] == 1:
                    #     freshMango = True
            print(grid)
            counter = counter + 1
            #print(counter)
        return counter-1


soln = Solution()
g = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]
print(soln.orangesRotting(g))