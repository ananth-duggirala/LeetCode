"""
Problem statement: https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3871/
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        curr = root
        if root == None:
            return []
        
        to_be_visited = [curr]
        inorder_traversal = [[curr.val]]
        
        while to_be_visited != []:
            temp = []
            for node in to_be_visited :
                for child in node.children:
                    temp.append(child)
            t = []
            for node in temp:
                t.append(node.val)
            if t!= []:
                inorder_traversal.append(t)
            to_be_visited = temp
            
        return inorder_traversal