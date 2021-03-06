"""
@author: Kaushik Acharya
"""
from typing import List

def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] and bfs(bfs,board, i, j, 0, word):
                    return True
                
        # print('Came from oustide')
        return False
        
def bfs(self,board: List[List[str]], i, j, count, word: str) -> bool:
    if count == len(word):
        return True
    
    # printcls(i, j, count)
    
    if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count]):
        # print('from bfs')
        return False
    # print(board[i][j])
    temp = board[i][j]
    board[i][j] = ''
    # print(temp)
    found = bfs(bfs, board, i + 1, j, count + 1, word) or bfs(bfs, board, i + 1, j, count + 1, word) or bfs(bfs, board, i, j + 1, count+1, word) or bfs(bfs, board, i, j - 1, count+1, word)
    # print(found)      
    board[i][j] = temp
    
    return found

input_1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

p = exist(exist, input_1, "ABCCED")
print(p)