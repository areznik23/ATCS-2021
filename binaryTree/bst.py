"""
Ms. Namasivayam
ATCS 2021-2022
Binary Tree

Python program to for binary tree insertion and traversals
"""
from bst_node import Node


'''
A function that returns a string of the inorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
def getInorder(root):
    if not root:
        return ''
    return getInorder(root.left) + str(root.val) + "-" + getInorder(root.right)


'''
A function that returns a string of the postorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
# A function to do postorder tree traversal
def getPostorder(root):
    if not root:
        return ''
    return getInorder(root.left) + getInorder(root.right) + str(root.val) + "-"


''' 
A function that returns a string of the preorder 
traversal of a binary tree. 
Each node on the tree should be followed by a '-'.
Ex. "1-2-3-4-5-"
'''
def getPreorder(root):
    if not root:
        return ''
    return str(root.val) + "-" + getInorder(root.left) + getInorder(root.right)


'''
A function that inserts a Node with the value
key in the proper position of the BST with the
provided root. The function will return the 
original root with no change if the key already
exists in the tree.
'''

# Not the cleanest function for this operation
# Edge case of when a null root is entered

def insert(root, key):
    if not root:
        return Node(key)

    def recur(root, key):
        if root.val == key:
            return
        if not root.left and key < root.val:
            root.left = Node(key)
            return
        if not root.right and key > root.val:
            root.right = Node(key)
            return
        if root.val < key:
            return recur(root.right, key)
        if root.val > key:
            return recur(root.left, key)

    recur(root, key)
    return root

'''
Challenge: A function determines if a binary tree 
is a valid binary search tree
'''
# Does not work at all - no output
# def isBST(root):
#
#     def left(root):
#         if not root.left:
#             return True
#         if root.left.val > root.val:
#             return False
#         return isBST(root.left)
#
#     def right(root):
#         if not root.right:
#             return True
#         if root.right.val > root.val:
#             return False
#         return isBST(root.right)



if __name__ == '__main__':
    # Tree to help you test your code
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(9)

    print("Preorder traversal of binary tree is")
    print(getPreorder(root))

    print("\nInorder traversal of binary tree is")
    print(getInorder(root))

    print("\nPostorder traversal of binary tree is")
    print(getPostorder(root))

    root = insert(root, 8)
    print("\nInorder traversal of binary tree with 8 inserted is")
    print(getInorder(root))

    root = insert(root, 23)
    print("\nInorder traversal of binary tree with 23 inserted is")
    print(getInorder(root))

    root = insert(None, 8)
    print("\nTesting a null root entry")
    print(getInorder(root))

