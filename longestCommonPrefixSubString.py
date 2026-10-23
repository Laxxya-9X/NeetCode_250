class Solution:
    def CommonPrefixSubString(self, arr):
        res =""
        for i in range(len(arr[0])):
            ch = arr[0][i]
            for j in range(1,len(arr)):
                if i >= len(arr[j]) or ch != arr[j][i]:
                    return res
            res+=ch
        return res       
s = Solution()
res = s.CommonPrefixSubString(["actors","actor","act"])
print(res)
