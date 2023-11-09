"""
Given the root of a binary search tree (BST) with duplicates, return all
 the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than 
    or equal to the node's key. 
    The right subtree of a node contains only nodes with keys greater 
    than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.

 

Example 1:

    [1]
      \
       [2]
      /
    [2]
    
Input: root = [1,null,2,2]
Output: [2]

Example 2:

Input: root = [0]
Output: [0]

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -105 <= Node.val <= 105
    
Follow up: Could you do that without using any extra space? (Assume that
the implicit stack space incurred due to recursion does not count).
"""
#Implementation for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    #Strategy: brute force recursions
    
    #Time complextiy: 
    #Space complexity: 

    def findMode(self, root = []) -> list[int]:
        self.maxCount = 1
        self.counts = {}
        self.modes = []
        def populateCounts(node):
            #count the current node
            if node.val in self.counts:
                self.counts[node.val] += 1
                if self.counts[node.val] > self.maxCount:
                    self.maxCount += 1
            else:
                self.counts[node.val] = 1
            if node.left:
                populateCounts(node.left)
            if node.right:
                populateCounts(node.right)
        
        populateCounts(root)
        for key in self.counts.keys():
            if self.counts[key] == self.maxCount:
                self.modes.append(key)
        return self.modes

if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(2), None))
    print(test.findMode(root))