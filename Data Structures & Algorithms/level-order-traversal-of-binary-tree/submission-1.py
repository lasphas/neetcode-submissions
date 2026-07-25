# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []

        res = []
        queue = collections.deque([root])

        while queue :
            size = len(queue)
            currlev = []

            for _ in range(size):
                node = queue.popleft() 
                currlev.append(node.val)

                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            
            res.append(currlev)
        return res


        