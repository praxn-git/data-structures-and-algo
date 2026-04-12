class stack:
    def __init__(self):
        self.list = []

# checking the length of the stack
    def length(self):
        print(f"The length of the stack is: {len(self.list)}")

# inserting element in the stack
  # method-01 -> via insert() method       
    def push(self, value):
        self.list.insert(0, value)

  # method-02 -> via append() method
    def append(self, value):
        self.list.append(value)

          
# peeking the top element of the stack      
    def peek(self):
        if len(self.list) == 0:
            raise Exception("Stack is empty!")
        else:
            return self.list[0]
    
# deleting the top element from the stack      
    def pop(self):
        if len(self.list) == 0:
            raise Exception("Stack is empty!")
        else: 
            return self.list.pop(0)
    
stack = stack()

# append and push functions
stack.append(10)
stack.append(20)
stack.push(30)
stack.push(40)

# pop and peek functions
stack.pop()
print(stack.peek())
stack.pop()
print(stack.peek())

# length functions
stack.length()