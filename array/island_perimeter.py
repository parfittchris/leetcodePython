class Solution:
    def islandPerimeter(self, grid):
        counter = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    pos = [row, col]
                    counter += (4 - self.findAdjacents(grid, pos))
        
        return counter


    def findAdjacents(self, grid, position):
        total = 0

        x = position[0]
        y = position[1]

        adjacents = [[0,1], [1,0], [0, -1], [-1, 0]]

        for el in adjacents:
            newX = x + el[0]
            newY = y + el[1]
            if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]):
                if grid[newX][newY] == 1:
                    total += 1
        
        return total
            

grid = [[0, 1, 0, 0],
 [1, 1, 1, 0],
 [0, 1, 0, 0],
 [1, 1, 0, 0]]

test = Solution()

print(test.islandPerimeter(grid))