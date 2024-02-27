##Units 4-9, LLs and DLLs

#SINGLY LINKED LISTS
#DEFINITION: Ordered set of data with pointer variables only for succceeding node.
#Important to understand that POINTERS like 'head', 'next', etc. are just variables
#That point to a node; the pointer itself is not a node object.

#Constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
#Print LL fxn
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
#Empty list fxn           
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
#Append node to list fxn        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
#Pop node from list fxn        
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
#Create new head for LL fxn
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
#Pop head from list fxn
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
#Get a node from LL fxn    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
#Set a new node value fxn
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
#Insert a new node at an input index fxn
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  
#Remove a node from LL at an input index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
#Reverse the list fxn    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True
    
##LINKED LIST EXERCISES
#Find Middle Node
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

##Detect Loop in Linked List
    def has_loop(self):
        slow = self.head
        fast = self.head
        while (slow != None and fast != None and fast.next != None):
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
        return False

#Partition list
    def partition_list(self, x):
        if not self.head:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            elif current.value > x:
                prev2.next = current
                prev2 = current
            current = current.next
        prev1.next, prev2.next = None, None
        prev1 = dummy2.next
        self.head = dummy1.next

#Remove Duplicates from Linked List
    def remove_duplicates(self):
        seen = set()
        prev= None
        current = self.head
        while current is not None:
            if current.value in seen:
                prev.next = current.next
                self.length -= 1
            else:
                seen.add(current.value)
                prev = current
            current = current.next
            
##Convert Binary to Decimal
    def binary_to_decimal(self):
            dec_val = 0
            while self.head:
                dec_val = 2*dec_val + self.head.value
                self.head = self.head.next
            return dec_val

#Find Kth Node from end in Linked List (NOT class method!!!)
#Takes linked list and kth node as inputs
def find_kth_from_end(ll, k):
    fast = ll.head
    slow = ll.head
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


##DOUBLY LINKED LISTS

#Constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
#Print the DLL
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
#Append a new node to DLL        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
#Pop from the DLL fxn
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length  -= 1
        return temp
#Add new head fxn    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
#Pop the head from the LL fxn
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp    
#Get a node at an input index fxn
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
#Set new value for existing node fxn        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
#Insert new node fxn    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True  
#Remove a node from a specific index fxn
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            temp = self.get(index)
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next, temp.prev = None, None
            self.length -= 1
            return temp
        
#DOUBLY LINKED LIST EXERCISES
#Swap head and tail in DLL
    def swap_first_last(self):
        if not self.head or self.head == self.tail:
            return
        else:
            self.head.value, self.tail.value = self.tail.value, self.head.value
            
#Reverse DLL
    def reverse(self):
        current_node = self.head
        while current_node:
            current_node.prev, current_node.next = current_node.next, current_node.prev
            current_node = current_node.prev
        self.head, self.tail = self.tail, self.head
        
#Check if DLL is Palindrome
    def is_palindrome(self):
        if self.length <= 1:
            return True
        forward_node, backward_node = self.head, self.tail
        for _ in range(self.length // 2):
            if forward_node.value != backward_node.value:
                return False
            else:
                forward_node = forward_node.next
                backward_node = backward_node.prev
        return True
    
#Swap Nodes in Pairs
#Little harder problem here.
    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next
            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            second_node.prev = previous_node
            first_node.prev = second_node
            if first_node.next:
                first_node.next.prev = first_node
            self.head = first_node.next
            previous_node = first_node
        self.head = dummy_node.next
        if self.head:
            self.head.prev = None
            
        
