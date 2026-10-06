arr = [2,3,7,9,11]
target = 12
def twosum(arr , target):
    left =0
    right =len(arr)-1
    while left < right:
            sum = arr[left]+arr[right]
            if sum == target:
                return [left , right]
            if sum < target:
                left+=1
            else:
                 right-=1

res = twosum(arr,target)
print(res)