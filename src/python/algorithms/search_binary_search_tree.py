"""
700. Search in a Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the 
subtree rooted with that node. If such a node does not exist, return null.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Searches for a node with the given value in a binary search tree.

        The function returns the subtree rooted with the node that has the 
        value val.
        If such a node does not exist, it returns None.

        The function uses the properties of a binary search tree to navigate
        through the tree efficiently.

        A binary search tree is a tree data structure in which each node has at 
        most two children.
        The left child of a node contains only nodes with values less than the 
        node's value, and the right child of a node contains only nodes with 
        values greater than the node's value.
        This property allows for efficient searching, insertion, and deletion 
        operations.

        The function uses recursion to traverse the tree. 
        It compares the value of the current node with the target value. 
        If they are equal, it returns the current node.
        If the target value is less than the current node's value, it recursively 
        searches in the left subtree.
        If the target value is greater than the current node's value, 
        it recursively searches in the right subtree.
        The function continues this process until it finds the node with the 
        target value or reaches a leaf node.

        The time complexity of this function is O(h), where h is the height of 
        the tree.
        The space complexity is O(h) due to the recursion stack.

        The function takes two parameters:
        1. root: The root of the binary search tree (BST)
        2. val: The value to search for in the BST
        """
        if not root:
            return None
        
        # Check if the current node's value matches the target value
        if val == root.val:
            return root
        # If the target value is greater than the current node's value,
        # search in the right subtree
        elif val < root.val:
            return self.searchBST(root.left, val)
        # If the target value is less than the current node's value,
        # search in the left subtree
        else:
            return self.searchBST(root.right, val)
        


# Example usage
if __name__ == "__main__":
    # Create a sample binary search tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    # Create an instance of the solution class
    solution = Solution()

    # Search for a value in the BST
    val_to_search = 2
    result_node = solution.searchBST(root, val_to_search)

    # Print the result
    if result_node:
        print(f"Node with value {val_to_search} found: {result_node.val}")
    else:
        print(f"Node with value {val_to_search} not found.")

# Time Complexity: O(h), where h is the height of the tree
# Space Complexity: O(h), where h is the height of the tree
# The space complexity is O(h) because of the recursion stack.
# In the case of a balanced tree, the height is log(n), where n is the 
# number of nodes.
# In the case of a skewed tree, the height is n.
# The time complexity is O(h) because we may have to traverse the height of 
# the tree in the worst case.


