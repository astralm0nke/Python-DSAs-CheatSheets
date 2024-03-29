#Idea: If you have 2 sorted lists, it's very easy to combine the two into one fully sorted list.
#Start with 1 item per list; then combine&sort pairs; keep repeating till one list.

#Merge is atually a HELPER FXN: takes values from 2 SORTED lists and combines into new sorted list
#variable i for 1st list, j for 2nd; compare&combine till one is empty

#CODE for MERGE helper- list1 and list2 must already be sorted
def _merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined
#^^^Uses while instead of for loops cuz u don't know how many iterations u need

#MERGE fnx- breaks lists in half to create 1 item 'sorted' lists
#Uses RECURSION- same thing over and over again&makes problem smaller
#Base Case: len(list) = 1; the uses merge helper to put everything back together

##CODE
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
#Each split becomes active instance on callstack
    return _merge(left, right)
#returns to what? Function that called it- eventually returns sorted list to original unsorted list fxn call

##Space & Time Complexity:
#Doubles items stored in memory: O(n) space complexity
#Unlike earlier in-place sorts, merge sort creates a new list
#Breaking apart Time complexity: O(log(n)); divide-and-conquer
#Putting back together TC: O(n)
#SO full time complexity: O(n*log(n))-> much more efficient than earlier O(n^2)

##EXERCISE
#Merge sort method for LinkedList that merges itself with an input list
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

    def merge(self, other_list):
        other_head = other_list.head
        dummy = Node(0)
        current = dummy
        
        while self.head is not None and other_head is not None:
            if self.head.value < other_head.value:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other_head
                other_head = other_head.next
                
            current = current.next
                
        if self.head is not None:
            current.next = self.head
        else:
            current.next = other_head
            self.tail = other_list.tail
                    
        self.head = dummy.next
        self.length += other_list.length
