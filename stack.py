#Question 10

class Node:
      
    def __init__(self):
        self.data = None
        self.next = None
  
class Stack:
    def __init__(self):
        self.head = None
    
 
    def smallestElement(self): 
  
        min = 32767
 
        while (self.head != None) :
      
            if (min > self.head.data) :
                min = self.head.data 
            self.head = self.head.next
      
        return min

     def push(self,data) :
    
        newNode = Node() 
    
        newNode.data = data 

        newNode.next = (self.head) 
    
        (self.head) = newNode 

    def printList(self) :
    
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        
    
stack = Stack()
stack.push( 15) 
stack.push( 14) 
stack.push( 13) 
stack.push( 22) 
stack.push( 17) 
print("Stack is : ") 
stack.printList() 
print("Minimum element in Stack: ",end="") 
print(stack.smallestElement(),end="") 
