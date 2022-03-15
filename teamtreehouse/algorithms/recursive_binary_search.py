# Video link: https://www.youtube.com/watch?v=8hly31xKli0
"""
Recursive solution - involves a set of stopping conditions and a function that calls itself.
e.g. functional languages don't like to do modification of variables and prefer a solution using recursion
"""

def recursive_binary_search(list, target):
  if len(list) == 0:
    return False
  else:
    midpoint = (len(list))//2
    
    if list[midpoint] == target:
      return True
    else:
      if list[midpoint] < target:
        return recursive_binary_search(list[midpoint+1:], target)
      else:
        return recursive_binary_search(list[:midpoint], target)

def verify(result):
  print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)