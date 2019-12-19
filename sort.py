arr = [5, 6, 1, 2, 3]

'''挿入ソート
分かり易い解説: https://www.youtube.com/watch?v=z0YcQIqyV5Q
'''
def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        ele = arr[i]
        while arr[j] > ele and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele
    return arr


'''選択ソート'''
def selection_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


'''バブルソート
最後にwhile文を通過するときには、既にソートされている
'''
def bubble_sort(arr):
    change = True
    # count = 0
    while change:
        # print(count)
        # print(arr)
        # count += 1
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr
print(bubble_sort(arr))