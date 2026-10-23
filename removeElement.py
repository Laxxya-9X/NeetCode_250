class Solution:
    def removeElement(self, nums, val):
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:     #comparing every ele with value if it is true
                nums[k] = nums[i]
                k += 1           
                
        return k

s =Solution()
nums = [1,2,3,4,3,2,2]
k = s.removeElement(nums,2)
print(k)
print(nums[:k])