mylist = []
for i in range(10000):
  mylist.append(i)

'''単純探索'''
def simple_search(list, item):
  for i in list:
    guess = i
    if guess == item:
      return item

'''二分探索'''
def binary_search(list, item):
  low = 0
  high = len(list) - 1
  while low <= high:
    mid = (high + low) // 2
    guess = list[mid]
    if guess == item:
      return item
    elif guess < list[mid]:
      low = mid + 1
    else:
      high = mid - 1
  return None # itemが存在しない

print(simple_search(mylist, 777))
