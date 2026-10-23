# Day 1 on neetcode
#================================================




class Solution:
    def two_Sum(self, nums, target):
        freq = {}
        for index , ele in enumerate(nums):
            remaining = target - ele
            if remaining in freq:
                return [freq[remaining],index]
            freq[ele] = index
        
        return []

s = Solution()
arr = list(map(int, input().split(",")))
tar = int(input("Enter target : "))
res = s.two_Sum(arr,tar)
print(res)


# Day 1 done