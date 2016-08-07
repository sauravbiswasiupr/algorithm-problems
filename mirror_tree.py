# Given a binary tree, invert it (mirror)

from BSTLib import *


def mirror_tree(root):
    if root is None:
        return

    mirror_tree(root.left)
    mirror_tree(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6]
    bst = BST(data=l)
    bst.inOrderTraversal(bst.root)
    print "Mirroring the tree"
    mirror_tree(bst.root)
    bst.inOrderTraversal(bst.root)