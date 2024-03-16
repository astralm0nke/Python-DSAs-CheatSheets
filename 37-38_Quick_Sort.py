##Quick Sort- idea is to start with a pivot point, then compare each item afterwards.
#Swaps smaller than pivot point with greater number; pivot point stays at list[0]
#Pivot point becomes first index of larger sublist thann last pivot

##Pivot: Sorts all values under pivot and above pivot value
#Uses a for loop & variables pivot_index and swap_index
#Move swap up one every time a smaller value is encountered again

##CODE    
#Pivot helper
def pivot(my_list, pivot_index, end_index):
    def swap(my_list, index1, index2):
        temp = my_list[index1]
        my_list[index1] = my_list[index2]
        my_list[index2] = temp
        
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
#Now need to swap items at pivot and swap index
    swap(my_list, pivot_index, swap_index)
    return swap_index

#Quick Sort final code
def quick_sort_helper(my_list, left, right):
    if left < right:
#^^^Base case
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)


##BIG O: pivot looks at each item- O(n)
#Quick Sort best case is O(n*log(n)); for unsorted list
#Worst case is O(n^2) bc running pivot fxn on every item when list is already sorted
#Remember that insertion sort is O(n)