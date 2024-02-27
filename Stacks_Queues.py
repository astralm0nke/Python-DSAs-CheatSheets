#Unit 10-12 STACKS & QUEUES
#STACKS
#Definition: Abstract data type that follows LIFO: Last In, First Out-> think can of pringles

#Constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
#Print stack fxn
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
#Add new node to top of stack fxn
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
#Delete top node and return fxn
    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
        return temp

#QUEUES
#Definition: Abstract data type that follows FIFO: First In, First Out
#Constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
#Print fxn
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
#Add node to queue fxn
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
#Remove node from queue fxn
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
    
#IMPLEMENTATIONS
#Implement Stack datatype using list
class Stack:
    def __init__(self):
        self.top = None
        self.height = 0
        self.stack_list = []
        
#Push the stack that uses a list
    def push(self, value):
        self.stack_list.append(value)
#See if empty
    def is_empty(self):
        return len(self.stack_list) == 0
#Check top value
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
#Check size
    def size(self):
        return len(self.stack_list)
#Add to stack_list
    def push(self, value):
        self.stack_list.append(value)
#Pop top of stack/list
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
    
#Check for balanced parentheses
    def is_balanced_parentheses(parentheses):
        stack = Stack()
        for p in parentheses:
            if p == '(':
                stack.push(p)
            elif p == ')':
                if stack.is_empty() or stack.pop() != '(':
                    return False
        return stack.is_empty()

#Reverse input string
def reverse_string(string):
    stack = Stack()
    reversed = ''
    for _ in string:
        stack.push(_)
    while not stack.is_empty():
        temp = stack.pop()
        reversed += temp
    return reversed

#Sort input stack
def sort_stack(stack):
    sorted_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            stack.push(sorted_stack.pop())
        sorted_stack.push(temp)
    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop())
        
#Queue using stacks
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
