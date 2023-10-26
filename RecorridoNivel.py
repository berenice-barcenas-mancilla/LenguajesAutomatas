from collections import deque
class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key=key
        self.left=left
        self.right=right
        
    def levelOrderTransversal(root):
        if not root:
            return