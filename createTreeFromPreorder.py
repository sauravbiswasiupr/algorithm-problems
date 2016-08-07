# Given an array of preorder traversal of a bst, generate the bst
from BSTLib import *


    # the code below is O(n**2)
    # for each node in the tree we check for partition in the pre array

def generateTreeFromPreorder(pre, low, high):
    if low == high:
        return TreeNode(pre[low])

    if low > high:
        return None

    higherIndex = findLeftRight(pre, low, high)
    root = TreeNode(pre[low])

    root.left = generateTreeFromPreorder(pre, low + 1, higherIndex - 1)
    root.right = generateTreeFromPreorder(pre, higherIndex, high)

    return root

## O(n) as key if in range is checked for all values in the pre array
## the index=[] is a workaround for using pointer like variable approaches
## in python

def generateTreeFromPreOrderOptimal(pre, min, max, size, index=[]):
    if index[0] >= size:
        return None

    key = pre[index[0]]

    if key > min and key < max:
        root = TreeNode(key)
        index[0] = index[0] + 1

        root.left = generateTreeFromPreOrderOptimal(pre, min, key, size, index)
        root.right = generateTreeFromPreOrderOptimal(pre, key, max, size, index)

        return root
    else:
        return None



def findLeftRight(pre, low, high):
    root = pre[low]
    breakIndex = None

    for i in range(low + 1, high + 1):
        if pre[i] > root:
            breakIndex = i
            break

    if breakIndex == None:
        return high + 1
    else:
        return breakIndex


if __name__ == "__main__":
    a = map(lambda x: int(x), raw_input().split(" "))
    n = len(a)
    root = generateTreeFromPreorder(a, 0, n-1)

    bst = BST()
    print "In order traversal..."
    bst.inOrderTraversal(root)
    print "Pre order traversal..."
    bst.preOrderTraversal(root)

    print "Optimal preorder creator..."
    root = generateTreeFromPreOrderOptimal(a, -100000, 100000, n, [0])
    print "In order travesal ..."
    bst.inOrderTraversal(root)
    print "Pre order traversal ..."
    bst.preOrderTraversal(root)