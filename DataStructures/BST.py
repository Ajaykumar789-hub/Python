#Rule in Binary search all nodes in left is less than top node and righ is create that top
#e.g
#    5
#   / \
#  4   7
# there is  3 ways in BST 1.Preorder(value,left,right) 2.Inorder(left,value,right) 3.post order(left,right,value)

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

def preorder(node):
    if not node:
        return None
    print(node.val)
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if not node:
        return None
    inorder(node.left)
    print(node.val)
    inorder(node.right)


def postorder(node):
    if not node:
        return None
    postorder(node.left)
    postorder(node.right)
    print(node.val)
    
def insert(node,x):
    if node is None:
        return x
    if node.val < x:
        node.right=insert(node.right,x)
    else:
        node.left=insert(node.left,x)
    return node    
    

def search(node,key):
    if node is None or node.val==key:
        return node
    if node.val<key:
        return search(node.right,key)
    else:
        return search(node.left,key)

node= Node(4, Node(2, Node(1), Node(3)), Node(6,None,Node(7)))
#            4
#          /   \
#         2     6
#       /   \     \
#      1    3      7
#preorder(node)
#inorder(node)
#postorder(node)
#print(search(node,9).val)
#insert(node,10)

def binarysearch(nums,low,high,x):
    
    if high<low:
        return None
    mid=(low+high)//2
    if nums[mid]==x:
       return mid
    elif nums[mid]>x:
        return binarysearch(nums,low,mid-1,x)
    else:
        return binarysearch(nums,mid+1,high,x)
    
nums=[1,2,3,4,5,6,7,8,9]

#print(binarysearch(nums,0,len(nums)-1,6))

# Given a binary search tree and a key, this function
# delete the key and returns the new root
 
 
"""def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root
 
    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
 
    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
 
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.key = temp.key
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
 
    return root
"""


    