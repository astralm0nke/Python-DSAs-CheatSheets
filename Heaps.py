#21-23, HEAPS
##DEFINITION: Tree-based data structure that satisfies the heap property: 
#In a max heap, for any given node C, if P is a parent node of C,
#then the key (the value) of P is greater than or equal to the key of C.

#^^^Node value always larger than children's values
#Unlike BST, you can have duplicates
#MAX HEAP: Highest value aat top: MIN HEAP: MinVal at top
#No guarantee to order of heap- not good for searching
#Stored in a list, does NOT use nodes, only integers
#Parent = Index / 2; Integer division if index 1 is empty; number always rounded down.

#CONSTRUCTOR
class MaxHeap:
    def __init__(self):
        self.head = []
    def _left_child(self, index):
        return (2 * index) + 1
    def _right_child(self, index):
        return (2 * index) + 2
    def _parent(self, index):
        return (index - 1) / 2
    def _swap(self, index1, index2):
       self.heap[index1], self.head[index2] = self.heap[index2], self.heap[index1]
#Insert item fxn
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
#Remove fxn ((U only ever remove top of heap)); always first make tree complete
    def remove(self):
#Need helper method called sink down
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value
#Sink Down helper fxn
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            if right_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if left_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
            
##Make the intuitive edits for Minimmum Heaps
#Farthest you'll ever have to sink down is height of tree
#Priority Queues
#O(log[n])

#EXERCISES

#Kth Smallest Element in an Array
def find_kth_smallest(nums, k):
    max_heap = MaxHeap()
    for num in nums:
        max_heap.insert(num)
        if len(max_heap.heap) > k:
            max_heap.remove()
    return max_heap.remove()

#Maximum Element in a Stream
def stream_max(lst):
    max_heap = MaxHeap()
    max_stream = []
    for i in lst:
        max_heap.insert(i)
        max_stream.append(max_heap.heap[0])
    return max_stream
            
