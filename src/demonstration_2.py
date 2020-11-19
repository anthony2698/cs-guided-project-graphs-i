"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.

You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque

def numIslands(grid):
    # Your code here
    # Iterate thorugh a our map
      # What do we do when we see a 1?
      # We need to figure out how large that island is
      # The island could just consist of a single 1, or 
      # it could have other 1's connections
      # When we encounter a 1, we need to traverse that island
      # By looking right and down
    
    # Over the course of traversing an island, how can we avoid
    # Double-counting 1's we've already seen before?
    # Toggle any 1's we've accounted for to a 0, to avoid double-counting
    # OR We can keep a separate data structure that keeps track of the coordinates that we've already visited

    num_islands = 0

    for i, row in enumerate(grid):
      for j, loc in enumerate(row):
        if loc == '1':
          num_islands += 1
          stack = [(i, j)]
          grid[i][j] = "0"

          while len(stack) > 0:
            r, c = stack.pop()

            if c < len(row) - 1 and grid[r][c + 1] == '1':
              stack.append((r, c + 1))
              grid[r][c + 1] = '0'

            if c < len(grid) - 1 and grid[r + 1][c] == '1':
              stack.append((r + 1, c))
              grid[r + 1][c] = '0'

    return num_islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","0","1","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))

            
            


      

