def linear_search(list, target):
# Returns index position if target found, else returns none
   for i in range(len(list)):
      if list[i] == target:
        return i
   return None

def verify(index):
   if index is not None:
      print("Target found at Index:", index)
   else:
      print("Target not found in the List")
    
numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 1)
verify(result)
      