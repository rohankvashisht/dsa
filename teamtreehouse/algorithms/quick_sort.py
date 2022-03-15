# Video link: https://www.youtube.com/watch?v=8hly31xKli0

"""
To check time : sum (User time + System time)
e.g. type in command line: 'time python quick_sort.py 5.txt'
"""

"""
Again, you can ignore these lines at the top. We're just using them to load a file full of numbers into a list.
"""
import sys
from load import load_numbers

numbers_folder_path = "../numbers/" + sys.argv[1]
numbers = load_numbers(numbers_folder_path)

"""
The Quicksort algorithm relies on recursion. To implement it, we'll write a recursive function. We'll accept the list of numbers to sort as a parameter.

Takes O(n^2) as worst case, O(n logn) as average case time.

If you pick a really bad pivot, the next recursive call to Quicksort will only reduce the list length by 1. Since our Quicksort function simply picks the first item to use as a pivot, we can make it pick the worst possible pivot repeatedly, simply by giving it a list that's sorted in reverse order. If we pick the worst possible pivot every time, we'll have to split the list once. For every item it contains, and then, do n-sorting operations on it.
"""
def quicksort(values):
  """
  Quicksort is recursive because it keeps calling itself with smaller and smaller subsets of the list you're trying to sort.
  
  We're going to need a base case where the recursion stops, so it doesn't enter an infinite loop.  Lists that are empty don't need to be sorted. And lists with just one element don't need to be sorted, either. In both cases, there's nothing to flip around.
  
  So we'll make that our base case; if there are 0 or 1 elements in the list passed to the "quicksort" function, we'll return the unaltered list to the caller.
  """
  if len(values) <= 1:
    return values
  
  """
  The code from here on out represents the recursive case. We need to create a list that will hold all the values less than the pivot. That list will be empty at first.
  """
  less_than_pivot = []
  
  # We do the same for values greater than the pivot.
  greater_than_pivot = []
  
  """
  Next we need to choose the pivot value. For now, we just grab the first item from the list.
  """
  pivot = values[0]
  
  """
  Then we loop through all the items in the list following the pivot.
  """
  for value in values[1:]:
    """
    We check to see whether the current value is less than or equal to the pivot.
    """
    if value <= pivot:
      # If it is, we copy it to the sub-list of values less than the pivot.
      less_than_pivot.append(value)
    # Otherwise, the current value must be greater than the pivot.
    else:
      greater_than_pivot.append(value) #So we copy it to the other list.
      
  
  """
  This last line is where the recursive magic happens. We call quicksort recursively on the sub-list that's less than the pivot. 

We do the same for the sub-list that's greater than the pivot. Those two calls will return sorted lists, so we combine the sorted values less than the pivot, the pivot itself, and the sorted values greater than the pivot. 

That gives us a complete, sorted list, which we return.
  """
  # print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
  return quicksort(less_than_pivot)+[pivot]+quicksort(greater_than_pivot)

"""
Lastly, we need to call our quicksort function with our list of numbers, and print the list it returns.
"""
# print(numbers)
sorted_numbers = quicksort(numbers)
print(sorted_numbers)