# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.maxPathSumVal = 0

    def search(self, node):

        if node.left is None and node.right is None:
            return node.val

        maxValue = node.val

        valLeft = 0
        if node.left is not None:
            valLeft = self.search(node.left)
            maxValue = max(maxValue, node.val + valLeft, valLeft)

        valRight = 0
        if node.right is not None:
            valRight = self.search(node.right)
            maxValue = max(maxValue, node.val + valRight, valRight)

        maxValue = max(
            maxValue,
            valLeft + node.val + valRight
        )

        self.maxPathSumVal = max(maxValue, self.maxPathSumVal)

        return max(valLeft + node.val, node.val, valRight + node.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSumVal = root.val
        self.search(root)
        return self.maxPathSumVal
