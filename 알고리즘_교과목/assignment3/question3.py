import math
#음의 무한대 표시해준것임
min = -math.inf
 
# bst단순 체크 이므로 bts삽입 과정을 구현하진 않았습니다 !

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
 
 
def isBST(root):
    global min
 
    if root:
        if not isBST(root.left):
            return False
 
        if root.data < min:
            return False
 
        min = root.data
        return isBST(root.right)

    return True

 
if __name__ == '__main__':
    root = Node(8)
    root.left = Node(3)
    root.right = Node(9)
    # root.right.left = Node('null')
    # root.right.right = Node('null')
    root.right.left = Node(4)
    root.right.right = Node(7)
 
    if isBST(root):
        print("The following binary tree is BST")
    else:
        print("The following binary tree is NOT BST")
 