"""
@author: Kaushik Acharya
"""
from typing import List


def minPathSum(self, grid: List[List[int]]) -> int:
    
    m = len(grid)
    n = len(grid[0])
    # arr=[]

    for i in range(0, m):
        # row_add=[]
        for j in range(0, n):
            if i == 0:
                if j != 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                    # row_add.append(grid[i][j-1] + grid[i][j])
                else:
                    # row_add.append(grid[i][j])   
                    continue
            else:
                if j !=0:
                    grid[i][j] = min(grid[i-1][j],grid[i][j-1])+ grid[i][j]
                else:
                    grid[i][j] = grid[i-1][j]+ grid[i][j]
                    # row_add.append(min(grid[i-1][j],grid[i][j-1])+ grid[i][j])
        # arr.append(row_add)
            
    print(grid)
    return grid[m-1][n-1]

