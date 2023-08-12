
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left
        
    def insert(node, x):
        if node is None:
            return node(x)
        if x < node.val:
            node.left =insert(node.left,x)
        else:
            node.right=insert(node.right,x)
        return node
    
node= Node(4, Node(2, Node(1), Node(3)), Node(6,None,Node(7)))
insert(node,3)