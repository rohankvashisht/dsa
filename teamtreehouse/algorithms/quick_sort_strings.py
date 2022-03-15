# Video link: https://www.youtube.com/watch?v=8hly31xKli0

"""
To check time : sum (User time + System time)
e.g. type in command line: 'time python quick_sort_strings.py unsorted.txt'
"""

"""
Again, you can ignore these lines at the top. We're just using them to load a file full of numbers into a list.
"""
import sys
from load import load_strings

names_folder_path = "../names/" + sys.argv[1]
names = load_strings(names_folder_path)

"""
We'll use our quicksort method to sort the list of names. Its code is completely unchanged from when you saw it in the previous stage.
"""
def quicksort(values):
  if len(values) <= 1:
    return values
  less_than_pivot = []
  greater_than_pivot = []
  pivot = values[0]
  for value in values[1:]:
    if value <= pivot:
      less_than_pivot.append(value)
    else:
      greater_than_pivot.append(value)
  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

"""
We just call our quicksort function on the list of names loaded from the file, and save the list to a variable.
"""
sorted_names = quicksort(names)
# Then, we loop through each name in the sorted list...
for n in sorted_names:
  # ...And print that name.
  print(n)