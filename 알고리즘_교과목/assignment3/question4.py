class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
  

def findLowestAncestor(root, left_node, right_node):
      
    if(root.data > left_node and root.data > right_node):
        return findLowestAncestor(root.left, left_node, right_node)
  
    
    if(root.data < left_node and root.data < right_node):
        return findLowestAncestor(root.right, left_node, right_node)
  
    return root
  

if __name__=="__main__":     
    root = Node(6)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.left.right.left = Node(7)
    root.left.right.right = Node(9)
    

    # 총 3회 반복
    first_one = 1 ; second_one = 3
    result = findLowestAncestor(root, first_one, second_one)
    print("the lowest ancestor of %d and %d is %d" %(first_one, second_one, result.data))

    first_one = 7 ; second_one = 9
    result = findLowestAncestor(root, first_one, second_one)
    print("the lowest ancestor of %d and %d is %d" %(first_one, second_one, result.data))

    first_one = 2 ; second_one = 8
    result = findLowestAncestor(root, first_one, second_one)
    print("the lowest ancestor of %d and %d is %d" %(first_one, second_one, result.data))
  
    