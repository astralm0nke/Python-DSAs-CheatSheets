##Units 16-18, HASH TABLES
##Definition: Associative Array of buckets, (dictionary!!!)
##Collision: When there's multiple values at the same hash/key. 2 common ways to deal with this:
#Separate Chaining- list of entries compose the value for the key with collisions
#Open Addressing: Uses Linear/Quadratic/etc. Probing to find next available bucket in data map.

#Class Constructor
class HashTable:
    def __init__(self, size = 7):
#Length of hash table should be a prime number; this increases randomness of distribution into buckets to reduce collisions
        self.data_map = [None] * size
#Hash fxn - computes index for {key: value}
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  
#Print fxn
    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
#Set fxn
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
#Get fxn
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
#Return hash table keys fxn
    def show_keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
##IMPLEMENTATION EXAMPLES

#Get item in common from two input lists
#Function creates a hash table for list1,
#Then iterates over list2 to see if any of its items are a key in the has table.
def item_in_common(list1, list2):
    dict = {}
    for i in list1:
        dict[i] = True
        
    for j in list2:
        if j in dict:
            return True
    return False

#Find Duplicates
# Creates a hash table with {num: count} & adds 1 to the count
#Via the built-in .get() method, if any keys have value > 1, added to list of duplicates.
def find_duplicates(nums):
    nums_dict = {}
    for num in nums:
        nums_dict[num] = nums_dict.get(num, 0) + 1
    duplicates = []
    for num, count in nums_dict.items():
        if count > 1:
            duplicates.append(num)
    return duplicates

#First Non-repeating Character in string
#Very similar to find_duplicates(); creates hash table of {char: count} & uses .get() to grab current count,
#Then add 1 to it for every sighting. If a char's count gets to 1, the character is returned.
def first_non_repeating_char(string):
    char_dict = {}
    for char in string:
        char_dict[char] = char_dict.get(char, 0) + 1
    for char in string:
        if char_dict[char] == 1:
            return char
    return None

#Find Anagrams in a List of Strings
#Uses built-in sorted() function to create a "canonical"(sorted a-z) form of a string,
#Adds the canonical string to hash table {canonical: [strings]}; because every sorted anagram will be the canonical,
#each anagram will be mapped to its canonical
#return a list of values
def group_anagrams(strings):
    anagram_groups = {}
    for strg in strings:
        canonical = ''.join(sorted(strg))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(strg)
        else:
            anagram_groups[canonical] = [strg]
    return list(anagram_groups.values())

#2sum Problem
#Pretty classic DSA leetcode/interview question. Takes a list of numbers and a target integer as inputs
#Uses Blt-In enumerate to get the index and number in list iteratively
#Each number has a complement that equals target when added to num
#Complement_map = {num: list index}
#Complement will be found bc each num is added w their indices to hash table
#So once a compliment is run that is a number in the HT, that means the Two Sum of target has been found.
def two_sum(nums, target):
    complement_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[num] = i
    return []

#Sum Subarray
def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if (current_sum - target) in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i   
    return []

#SETS
#Definition: Unordered, mutable, iterable data type with no duplicates!!!!

#Remove Duplciates in a List
#Simple function that just takes an input list, uses the Blt-In fxn set() to turn it into a set, then uses Btl-In list() to return to list
#Set() function doesn't allow duplicates
def remove_duplicates(llist):
    new_list = list(set(llist))
    return new_list

#Unique Characters in a String
#Creates empty set chars, then iterates over input string to add each char to set
#Bc sets don't allow duplicates, if a char is already in the set, it returns False.
def has_unique_chars(strg):
    chars = set()
    for char in strg:
        if char in chars:
            return False
        chars.add(char)
    return True

#Find Pairs between Arrays
#Takes 2 arrays & a target sum between them.
#Turns array1 into a set & initializes an empty list of pairs
#If compliment between target and num in array2 found in set1, the pair is appended to the pair list
def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs

#Find Longest Consecutive Sequence
def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_seq = 0
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_seq = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_seq += 1
            longest_seq = max(longest_seq, current_seq)
    return longest_seq
