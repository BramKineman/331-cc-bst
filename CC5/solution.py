"""
CC5- Trie
Name: Bram Kineman
"""

from __future__ import annotations  # allow self-reference

from typing import Tuple
import sys


class TreeNode:
    """Tree Node that contains a value as well as left and right pointers"""

    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


def game_master(root: TreeNode) -> int:
    """
    Method that finds the largest valued valid BST within a potentiall invalid BST.
    :param root: TreeNode root of BST.
    """
    #  current sum, max of left subtree, min right subtree,
    def inner(node: TreeNode, running_total: int) -> Tuple[int, int, int]:
        """
        Inner helper method that runs through a BST in a postorder fashion,
        keeping track of the greatest sum of a validated BST.
        :param node: TreeNode
        :param running_total: sum of node values in valid BSTs.
        """
        nonlocal res  # keep track of max answer
        if node is None:
            return 0, sys.maxsize, -sys.maxsize

        # post order
        left_total, min_left, max_left = inner(node.left, running_total)
        right_total, min_right, max_right = inner(node.right, running_total)

        # logic, starting at bottom left leaf
        new_max = max(max_left, max_right, node.val)
        new_min = min(min_left, min_right, node.val)

        if not max_left < node.val < min_right:  # invalid bst
            return max(left_total, right_total), -sys.maxsize, sys.maxsize

        return left_total + right_total + node.val, new_min, new_max

    # OUTSIDE INNER
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val
    res = inner(root, 0)
    return max(res[0], 0)
