class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def solve(root):
    def travel_next(node, parent):
        while parent.next: 
            parent = parent.next
            if parent.left: return parent.left
            if parent.right: return parent.right
        return None
    
    def recur(node, parent):
        if not node: return
        if node is parent.left and (parent.right):
            node.next = parent.right
        else:
            node.next = travel_next(node, parent)
        recur(node.right, node)
        recur(node.left, node)
    recur(root, Node(-1))
    return root

root = Node(0)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.right.left = Node(3)
root.right.right = Node(-1)
root.left.left.left = Node(5)
root.left.left.right = Node(1)
root.right.left.right = Node(6)
root.right.right.right = Node(8)

solve(root)