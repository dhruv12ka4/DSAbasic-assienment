# Question 9

class Node:
	
	def __init__(self, data, next):
		self.data = data
		self.next = next

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data, self.head)
        self.head = new_node
	
    def reverseList(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            self.head = prev
        return self.head

     def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

if __name__ == "__main__":
    
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print("Original stack : \n")
    stack.printList()
    stack.reverseList()
    print("\nReversed stack :\n")
    stack.printList()
