#delete a node from list, you are given access only to that node and not to the head node

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
    
    def deleteNode(self, node: Node):
        temp = node
        while temp.next != None:
            temp.data = temp.next.data
            node = temp
            temp = temp.next
        node.next = None

myList = LinkList()
size = int(input("Enter size of list"))
for i in range(size):
    val=int(input(f"Enter {size - i} value"))
    myList.add(val)
myList.display()

temp = myList.head
for i in range(3):
    temp = temp.next
myList.deleteNode(temp)

print("After deleting")
myList.display()
