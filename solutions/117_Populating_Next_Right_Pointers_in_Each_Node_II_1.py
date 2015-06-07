# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        p = root.next
        while p != None:
            if p.left != None:
                p = p.left
                break
            if p.right != None:
                p = p.right
                break
            p = p.next
        if root.right != None:
            root.right.next = p
        if root.left != None:
            root.left.next = root.right if root.right else p
        self.connect(root.right)
        self.connect(root.left)