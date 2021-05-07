import random 

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self, head=None):
        self.head = head

    def insert(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node


    def deleteDuplicate(self):

        cur = self.head
        prev = None

        stored_duplicate = {}
        while cur:
            if cur.data not in stored_duplicate:
                stored_duplicate[cur.data] = None
                prev = cur
            else:
                prev.next = cur.next

            cur = cur.next
    

    
    def printLinkedList(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ->")
            cur = cur.next
        print("\n")

if __name__=="__main__":  
    llist = LinkedList()
    # 정렬안된 노드 20개 채워넣기
    llist.insert(20)
    llist.insert(11)
    llist.insert(17)
    llist.insert(29)
    llist.insert(3)
    llist.insert(5)
    llist.insert(7)
    llist.insert(21)
    llist.insert(11)
    llist.insert(18)
    llist.insert(10)
    llist.insert(20)
    llist.insert(4)
    llist.insert(6)
    llist.insert(8)
    llist.insert(24)
    llist.insert(24)
    llist.insert(22)
    llist.insert(1)

    print("[original] an unsorted linked list:")
    llist.printLinkedList()

    print("[change] remove duplicates from an unsorted linked list:")
    llist.deleteDuplicate()
    llist.printLinkedList()