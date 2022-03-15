# Video link: https://www.youtube.com/watch?v=8hly31xKli0

"""
The function takes a list of the numbers we want to add.
"""
def sum_non_recursive(numbers):
  # The total starts at zero.
  total = 0
  # We loop over every number contained in the list.
  for number in numbers:
    # And we add the current number to the total.
    total += number
  # Once we're done looping, we return the accumulated total.
  return total

"""
If we call the sum function with a list of numbers, it will return the total. When we run this program it will print out that returned value, "19".
"""
print("Sum obatined in non-recursive manner: ", sum_non_recursive([1, 2, 7, 9]))


"""
It will take the list of numbers to add, just like before.
"""
def sum_recursive(numbers):
  """
  Python treats a list that contains one or more values as a "true" value, and it treats a list containing _no_ values as a "false" value. So we'll add an "if" statement that says if there are no numbers in the list, we should return a sum of 0. That way, the function will exit immediately, without making any further recursive calls to itself.
  """
  if not numbers:
    return 0

  print("Calling sum (%s)" % numbers[1:])
  """
  Now here's the recursive part. We'll have the "sum_recursive" function call itself. We use slice notation to pass the entire list of numbers EXCEPT the first one.
  """
  remaining_sum = sum_recursive(numbers[1:])
  
  print("Call to sum(%s) returning %d + %d" % (numbers, numbers[0], remaining_sum))
  
  """
  Then we add the first number in the list to the result of the recursive function call, and return the result.
  """
  return numbers[0] + remaining_sum

print("Sum obatined in recursive manner: ", sum_recursive([1, 2, 7, 9]))