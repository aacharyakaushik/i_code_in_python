"""
@author: Kaushik Acharya
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    
    pre_len = len(preorder)
    in_len = len(inorder)
    
    if pre_len != in_len or preorder is None or inorder is None or pre_len == 0:
        return None
    
    root = TreeNode(preorder[0])
    root_index = inorder.index(root.val)
    
    root.left = buildTree(buildTree, preorder[1:root_index+1], inorder[:root_index])
    root.right = buildTree(buildTree, preorder[root_index+1:],inorder[root_index+1:])

    return root


p = buildTree(buildTree,[3,9,20,15,7],[9,3,15,20,7])
print(p)