# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        # print(queue[0].val)
        ans = []
        level_size = 1
        while queue:
            subans = []
            
            for _ in range(level_size):
                node = queue.popleft()
                subans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_size = len(queue)
            print(level_size)
            ans.append(subans)
            

        return ans
