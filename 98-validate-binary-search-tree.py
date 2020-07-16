class Solution:
    def isValidBST(
        self, root: TreeNode, lower=float("-inf"), higher=float("inf")
    ) -> bool:

        return (
            not root
            or lower < root.val < higher
            and self.isValidBST(root.left, lower, root.val)
            and self.isValidBST(root.right, root.val, higher)
        )
