class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert(self, val):
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
            temp = temp.next

    def makeCircular(self, n):
        temp = self.head
        count = 0
        while temp.next != None:
            if count == n:
                temp2 = temp
            temp = temp.next
            count += 1
        temp.next = temp2


    def Loop(self):
        fast = self.head
        slow = self.head
        flag = 0


        while fast != None and (slow != fast or flag == 0):
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
                flag = 1

        if fast == None:
            print("List is not circular")
            return
        
        slow = self.head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        print("Start of the loop is ", slow.data)

length = int(input("Enter the node to create circular list"))
usrList1 = LinkList()
for i in range(length):
    val = int(input(f"Enter value {i}:"))
    usrList1.insert(val)

usrList1.display()

length = int(input("Enter the size of the list 1"))
usrList1.makeCircular(length)
usrList1.Loop()