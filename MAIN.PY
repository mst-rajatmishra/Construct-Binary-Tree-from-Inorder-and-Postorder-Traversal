  # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        # Create a dictionary to store the index of each value in inorder
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        
        def build(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None
            
            # The last element in postorder is the root
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            # Find the index of the root in inorder
            root_index = inorder_index[root_val]
            
            # Number of elements in the left subtree
            left_size = root_index - in_start
            
            # Recursively build the left and right subtrees
            root.left = build(in_start, root_index - 1, post_start, post_start + left_size - 1)
            root.right = build(root_index + 1, in_end, post_start + left_size, post_end - 1)
            
            return root
        
        # Start building the tree
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
