
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


def palindrome(List1:LinkList):
    stack = []
    temp = List1.head
    while temp != None:
        stack.insert(0,temp.data)
        temp = temp.next

    print(stack)
    List1.display()
    temp = List1.head
    while temp != None:
        if temp.data != stack.pop(0):
            return False
        temp = temp.next
    
    return True

def palinRecursion(ptr: Node,N,ind):
    if ind == N // 2:
        if N % 2 == 0:
            print(ptr.data)
            return True, ptr
        else:
            return True, ptr.next
    
    Res, temp = palinRecursion(ptr.next,N, ind+1)
    if ptr.data == temp.data:
        return (True and Res), temp.next
    else:
        return False, temp.next


length = int(input("Enter the size of the list 1"))
usrList1 = LinkList()
for i in range(length):
    val = int(input(f"Enter value {i}:"))
    usrList1.insert(val)
# Res = palindrome(usrList1)
Res, node = palinRecursion(usrList1.head, length, 0)
print(Res)


    

