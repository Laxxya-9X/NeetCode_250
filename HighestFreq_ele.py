class Solution:
    def majorityElement(self, nums):
        freq = {}
        max_count = 0
        max_ele = nums[0]
        for ele in nums:         #sabse phle dictionary me inki freq store krwa leta hu
            if ele in freq:
                freq[ele]+=1
            else:
                freq[ele] = 1
        
        for  k in freq:         # jitni keys hongi utni bar chlana hai or jis key ki high freq hogi use max ele me dal dena hai
            if freq[k]> max_count:
                max_count = freq[k]
                max_ele = k
        return max_ele
s = Solution()
print(s.majorityElement([2,2,2,2,4,4,4,5,2,1,6]))        