#!/usr/bin/env python3
'''
  Inductive definition of the function
    fun3(0) is 5
    fun3(1) is 7
    fun3(2) is 11
    func3(n) is fun3(n-1) + fun3(n-2) + fun3(n-3)

  Solution 1: Straightforward but exponential
'''
def fun3_1(n: int) -> int:
    result = None
    
    if n == 0:
        result = 5       # Base case
    elif n == 1:
        result = 7       # Base case
    elif n == 2:
        result = 11      # Base case
    else:
        result = fun3_1(n-1) + fun3_1(n-2) + fun3_1(n-3) # Recursive case
    return result

'''
  Solution 2: New helper recursive function makes it linear
'''
def fun3(n: int) -> int:
    ''' Recursive core. 
        fun3(n) = _fun3(n-i, fun3(2+i), fun3(1+i), fun3(i)) 
    '''
    def fun3_helper_r(n: int, f_2: int, f_1: int, f_0: int):
        result = None
        if n == 0:
            result = f_0     # Base case
        elif n == 1:
            result = f_1     # Base case
        elif n == 2:
            result = f_2     # Base case
        else:
            result = fun3_helper_r(n-1, f_2+f_1+f_0, f_2, f_1) # Recursive step
        return result

    return fun3_helper_r(n, 11, 7, 5)

''' binary_strings accepts a string of 0's, 1's, and X's and returns a
   generator that goes through all possible strings where the X's
   could be either 0's or 1's. For example, with the string '0XX1',
   the possible strings are '0001', '0011', '0101', and '0111'
'''
from typing import List, Generator
def binary_strings(string: str) -> Generator[str, None, None]:

    def _binary_strings(string: str, binary_chars: List[str], idx: int):
        if idx == len(string):
            yield ''.join(binary_chars)
            binary_chars = [' ']*len(string)
        else:
            char = string[idx]
            if char != 'X':
                binary_chars[idx]= char
                yield from _binary_strings(string, binary_chars, idx+1)
            else:
                binary_chars[idx] = '0'
                yield from _binary_strings(string, binary_chars, idx+1)
                binary_chars[idx] = '1'
                yield from _binary_strings(string, binary_chars, idx+1)
        

    binary_chars = [' ']*len(string)
    idx = 0
    yield from _binary_strings(string, binary_chars, 0)

''' Recursive KnapSack: You are looking to rob a jewelry store. You
have been staking it out for a couple of weeks now and have learned
the wieghts and values of every item in the store. You are looking to
get the biggest score you possibly can but you are only one person and
your backpack can only fit so much. Write a function that accepts a
list of items as well as the maximum capacity that your backpack can
hold and returns a list containing the most valuable items you can
take that still fit in yoyur backpack.  '''

from typing import List
class Item(object):
    def __init__(self, name: str, weight: int, value: int) -> None:
    	self.name = name
    	self.weight = weight
    	self.value = value
 
    def __lt__(self, other: "Item"):
    	if self.value == other.value:
            if self.weight == other.weight:
            	return self.name < other.name
            else:
            	return self.weight < other.weight
    	else:
     	    return self.value < other.value
 
    def __eq__(self, other: "Item") -> bool:
    	if isinstance(other, Item):
            return (self.name == other.name and
                    self.value == other.value and
                    self.weight == other.weight)
    	else:
            return False
 
    def __ne__(self, other: "Item") -> bool:
    	return not (self == other)
 
    def __str__(self) -> str:
    	return f'A {self.name} worth {self.value} that weighs {self.weight}'

def get_best_backpack(items: List[Item], max_capacity: int) -> List[Item]:

    def get_best_r(took: List[Item], rest: List[Item], capacity: int) -> List[Item]:
        if not rest or not capacity:    # Base case
            return took
        else:
            item = rest[0]
            list1 = []
            list1_val = 0
            if item.weight <= capacity:
                list1 = get_best_r(took+[item], rest[1:], capacity-item.weight)
                list1_val = sum(x.value for x in list1)

            list2 = get_best_r(took, rest[1:], capacity)
            list2_val = sum(x.value for x in list2)
            return list1 if list1_val > list2_val else list2

    return get_best_r([], items, max_capacity)
