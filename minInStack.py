class Node:
    def __init__(self, val):
        self.data = val
        self.min = val
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, val):
        node = Node(val)
        if self.top != None:
            if self.top.min < node.min:
                node.min = self.top.min
        node.next = self.top
        self.top = node
    
    def pop(self):
        if self.top == None:
            print("Stack Empty")
            return -1
        val = self.top.data
        self.top = self.top.next
        return val
    
    def display(self):
        temp = self.top
        while temp != None:
            print(temp.data, end="->")
            temp=temp.next
    
    def findMin(self):
        return self.top.min
    def peek(self):
        return self.top.data
    
class Stack2:
    def __init__(self):
        self.top = None
        self.min = Stack()
        
    def push(self, val):
        node = Node(val)
        if self.top != None:
            if self.min.top.data > node.data:
                self.min.push(val)
        else:
            self.min.push(val)
        node.next = self.top
        self.top = node
    
    def pop(self):
        if self.top == None:
            print("Stack Empty")
            return -1
        if self.min.top.data == self.top.data:
            self.min.pop()
        val = self.top.data
        self.top = self.top.next
        return val
    
    def display(self):
        temp = self.top
        while temp != None:
            print(temp.data, end="->")
            temp=temp.next
    
    def findMin(self):
        return self.min.peek()
    
length = int(input("Enter the number of elements in stack"))
stack = Stack2()
for i in range(length):
    stack.push(int(input(f"Enter the value {i}")))

for i in range(length - 4):
    print(f"The minimum at level {length - i} is ",stack.findMin())
    print(f"The vlaue at level {length - i} is ",stack.pop())

stack.display()