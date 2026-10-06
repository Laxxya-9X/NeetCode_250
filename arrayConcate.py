def arrayConcate(arr):
    for i in range(len(arr)):
        arr.append(arr[i])
    return arr
nums = [1,2,3,4]

res = arrayConcate(nums)
print(res)