# Partition a list based on a given value


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    
class LinkList:
    def __init__(self):
        self.head = None
    
    def add(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def display(self):
        temp = self.head

        while temp != None:
            print(temp.data,end='->')
            temp =temp.next

    def partition(self, val):
        fastPtr = self.head
        slowPtr = self.head

        while(fastPtr != None):
            if fastPtr.data < val:
                temp = slowPtr.data
                slowPtr.data = fastPtr.data
                fastPtr.data = temp
                slowPtr = slowPtr.next
            fastPtr = fastPtr.next

myList = LinkList()
size = int(input("Enter size of list"))
for i in range(size):
    val=int(input(f"Enter {size - i} value"))
    myList.add(val)
myList.display()

print("After Partition")
myList.partition(5)
myList.display()