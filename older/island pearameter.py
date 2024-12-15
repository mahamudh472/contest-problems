class Solution:
    def islandPerimeter(self, grid) -> int:
        result = 0
        for i in range(len(grid)):
            for x in range(len(grid[i])):
                top = False
                left = False
                if grid[i][x] == 1:
                    result += 4
                    if i>0 and grid[i-1][x]==1:
                        top = True
                    if x>0 and grid[i][x-1]==1:
                        left = True
                if top and left:
                    result -= 4
                elif top or left:
                    result -= 2
        return result

sol = Solution()
print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))