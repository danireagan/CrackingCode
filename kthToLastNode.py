# Find kth to Last node of the list

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        NewNode = Node(val)
        if self.head == None:
            self.head = NewNode
        else:
            # curNode = self.head
            NewNode.next = self.head
            self.head = NewNode
        
    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.data,end='->')
            temp = temp.next

    # Recursive approach
    def recursiveKtoLast(self, ptr: Node , k) -> int:
        if ptr == None:
            return 0
        
        i = self.recursiveKtoLast(ptr.next, k) + 1
        if i == k:
            print(ptr.data)
        return i
    
    # Two pointer approach
    def twoPointerKtoLast(self, k):
        fastPtr = self.head
        slowPtr = self.head
        ind = 0

        while fastPtr != None:
            if ind >= k:
                slowPtr = slowPtr.next
            fastPtr = fastPtr.next
            ind = ind + 1
        
        print(slowPtr.data)

myList = LinkList()
size = int(input("Enter size of list"))
for i in range(size):
    val=int(input(f"Enter {size - i} value"))
    myList.insert(val)
myList.printl()
k = int(input("Enter k value"))
myList.recursiveKtoLast(myList.head,k)
print("Two Pointer")
myList.twoPointerKtoLast(k)





