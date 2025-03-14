# Write a method to remove duplicates from an unsorted linked list

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Add at the end
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = newNode


    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data, end='->')
            temp = temp.next
            
    def removeDuplicates(self):
        temp = self.head
        hashTable = {}
        prev = None

        while temp != None:
            if prev == None:
                hashTable[temp.data] = 1
                prev = temp
            else:
                val = hashTable.get(temp.data,0)
                # print(val)
                if val == 0:
                    hashTable[temp.data] = 1
                    prev = temp
                else:
                    prev.next = temp.next
                    print("removing")
                    # print(prev.data)
                    print(prev.data,temp.data)
                    
            temp = temp.next

    def removeDuplicates2(self):
        temp1 = self.head
        prev = None
        while temp1 != None:
            temp2 = temp1.next
            prev = temp1
            while temp2 != None:
                if temp1.data == temp2.data:
                    prev.next = temp2.next
                else:
                    prev = temp2
                temp2 = temp2.next
            temp1 = temp1.next

length = int(input("Enter the size of the list"))
usrList = LinkedList()
for i in range(length):
    val = int(input(f"Enter value {i}:"))
    usrList.append(val)

usrList.display()
usrList.removeDuplicates2()
print("After removing duplicates")
usrList.display()

