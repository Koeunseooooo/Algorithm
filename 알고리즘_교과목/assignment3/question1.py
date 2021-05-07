import random

class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
 
    def __init__(self):
        self.head = None
 
    def reverse(self):
        prev = None
        cur = self.head
        while(cur is not None):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
 
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
 
    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ->')
            temp = temp.next
        print("\n")

    def append(self,data):
        new_node= Node(data)
        cur=self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def remove(self,index):
        inx_th=0


        cur=self.head
        prev =None
        next =self.head.next
        if index == 0:
            self.head = next
        else:
            while inx_th < index :
                if cur.next:
                    prev = cur
                    cur = next
                    next = next.next
                else:
                    break
                inx_th += 1
            if inx_th == index:
                prev.next= next
            else:
                return -1
 
 
if __name__=="__main__":
    llist = LinkedList()
    for i in range(10):
        llist.insert(random.randint(0,50))
    print("origin linked list:")
    llist.traverse()

    print("insert data 3:")
    llist.insert(3)
    llist.traverse()

    print("append data 5t:")
    llist.append(5)
    llist.traverse()

    print("remote 3th index data:")
    llist.remove(3)
    llist.traverse()

    print("reverse :")
    llist.reverse()
    llist.traverse()
    
