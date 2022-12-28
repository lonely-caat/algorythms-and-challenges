a = [6,4,3,8,91,1]

def sort_it(arr):
    for element in range(len(arr)-1):
        for el in range(len(arr)-element-1):
            if arr[el] > arr[el+1]:
                arr[el], arr[el+1] = arr[el+1], arr[el]
    return arr

print(sort_it(a))