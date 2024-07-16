def check_arr(arr):
    for i in range(len(arr)-1):
        if arr.count(arr[i]) != arr.count(arr[i-1]):
            return True
        else:
            return False



# arr = [1, 2, 2, 1, 1, 3]
# arr = [1, 2]
arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
# arr = [1, 2, 1, 2]

print(check_arr(arr))

