# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        def helper(node, level, dict_repr):
            if not node:
                return
            dict_repr[level].insert(0, node.val)
            helper(node.right, level + 1, dict_repr)
            helper(node.left, level + 1, dict_repr)

        dict_repr = defaultdict(list)
        helper(root, 0, dict_repr)
        return list(reversed(dict_repr.values()))
