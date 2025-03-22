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


def intersecting(List1:LinkList, List2:LinkList):
    temp = List1.head
    len1 = 0
    while temp != None:
        len1+=1
        temp = temp.next
    len2 = 0
    temp = List2.head
    while temp != None:
        len2+=1
        temp = temp.next
    
    
    if len1 > len2:
        head = List1.head
        count = len1 - len2
        tail = List2.head
    else:
        head = List2.head
        count = len2 - len1
        tail = List2.head
    
    for i in range(count):
        head = head.next
    
    print(head.data)
    flag = 0
    while head != None:
        if head.data == tail.data and head.next == tail.next:
            if flag == 0:
                start = head
                flag = 1
        else:
            flag = 0
        
        head = head.next
        tail = tail.next
    
    if flag == 0:
        return None
    else:
        return start
    
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

# usrList2.head = usrList1.head.next

res = intersecting(usrList1,usrList2)
if res == None:
    print("List are not intersecting")
else:
    print("intersecting from ", res.data)
    temp = res
    while temp != None:
        print(temp.data)
        temp = temp.next


