# sum the numbers represented in two lists. 5 -> 2 -> 1  + 2 -> 3 -> 2 = 7 -> 5 -> 4

class Node:
    def __init__(self, val):
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
    
    def add(self, head2: Node):
        if self.head == None:
            return head2
        elif self.head != None and head2 == None:
            return self.head
        else:
            head3 = Node(0)
            temp = head3
            ptr1 = self.head
            ptr2 = head2
            carry = 0

            while ptr1 != None and ptr2 != None:
                temp.data = ptr1.data + ptr2.data + carry
                carry = temp.data // 10
                temp.data = temp.data % 10
                temp.next = Node(0)
                prev = temp
                temp = temp.next
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            while ptr1 != None:
                temp.data = ptr1.data + carry
                carry = temp.data // 10
                temp.data = temp.data % 10
                temp.next = Node(0)
                prev = temp
                temp = temp.next
                ptr1 = ptr1.next
            
            while ptr2 != None:
                temp.data = ptr2.data + carry
                carry = temp.data // 10
                temp.data = temp.data % 10
                temp.next = Node(0)
                prev = temp
                temp = temp.next
                ptr2 = ptr2.next
            
            if carry == 1:
                temp.data = 1
            else:
                prev.next = None
            return head3

def recursion(ptr1 : Node,ptr2: Node):
    if ptr1 == None and ptr2 == None:
        return 0, None
    temp = Node(0)
    carry, node = recursion(ptr1.next,ptr2.next)
    temp.next = node
    temp.data = ptr1.data + ptr2.data + carry
    carry = temp.data // 10
    temp.data = temp.data % 10
    return carry, temp

def addForward(List1: LinkList, List2: LinkList):
    temp = List1.head 
    temp2 = List2.head
    length1 = 0
    length2 = 0
    while temp != None:
        length1 += 1
        temp = temp.next
    
    while temp2 != None:
        length2 += 1
        temp2 = temp2.next

    count = 0
    count = length2 - length1
    if count > 0:
        headTemp = List1.head
    elif count < 0:
        count = length1 - length2
        headTemp = List2.head
    
    for _ in range(count):
        temp = Node(0)
        temp.next = headTemp
        headTemp = temp
    
    if length2 - length1 > 0:
        List1.head = headTemp
    elif length1 - length2 > 0:
        List2.head = headTemp
    
    print("List 1")
    List1.display()
    print("List 2")
    List2.display()

    carry = 0
    head3 = Node(123)
    carry, head3 = recursion(List1.head,List2.head)
    res = LinkList()
    if carry == 1:
        temp = Node(1)
        temp.next = head3
        res.head = temp
    else:    
        res.head = head3

    return res

        
length = int(input("Enter the size of the list 1"))
usrList1 = LinkList()
for i in range(length):
    val = int(input(f"Enter value {i}:"))
    usrList1.insert(val)

length = int(input("Enter the size of the list 2"))
usrList2 = LinkList()
for i in range(length):
    val = int(input(f"Enter value {i}:"))
    usrList2.insert(val)

usrList1.display()
print("List 2")
usrList2.display()

usrList3 = LinkList()
# usrList3.head = usrList1.add(usrList2.head)
res = addForward(usrList1,usrList2)
print("After addition")
res.display()
