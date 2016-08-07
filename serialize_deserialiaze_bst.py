# Serialize and deserialize a binary (search) tree. Use preorder traversal, for each internal node use a special
# character i.e ' after the value of that node. For each leaf node use the value of that node only. Each null character
# is signified by a / mark. An internal node is one which has two children or atleast one child. The null character
# is used  when the node has one child.

from BSTLib import *


def serialize_tree(node, f):
    if not node:
        f.write("/")
        return

    # if node is a leaf node
    if node.left is None and node.right is None:
        f.write(str(node.data))
        return

    # node must have atleast one child.
    f.write(str(node.data) + "'")

    serialize_tree(node.left, f)
    serialize_tree(node.right, f)


def deserialize_tree(s):
    if not s:
        return None

    if s[0] == "/":
        return None
    else:
        return TreeNode(s[0])

    root = None
    if s[1] == "'":
        root = TreeNode(s[:2])
    root.left = deserialize_tree(s[2:])

    #


if __name__ == "__main__":
    node = TreeNode(1)
    node.right = TreeNode(3)
    f = open("serialized_tree.txt", "w")
    serialize_tree(node, f)
    f.close()
