class Solution:

    
    # def sortingString(self,ele): # me bubble sort use kr rha hu
    #     chars = list(ele)
    #     n = len(chars)
    #     for i in range(n):      
    #         for j in range(0,n-i-1):
    #             if chars[j] > chars[j+1]:
    #                 chars[j],chars[j+1] =chars[j+1], chars[j]
    #     return "".join(chars)       # Oops TLE kyuki bhaiya hume time complexity km krna  hai to ab me isko comment krunga or count sort use krunga
    
    def count_sortingString(self,ele):
        count = [0]*26
        for ch in ele:
                count[ord(ch) - ord('a')]+=1
        sorted_str = ""
        for i in range(26):
            sorted_str+=chr(i + ord('a'))*count[i]
        return sorted_str
    
    def groupAnagrams(self, strs):
        frq = {}
        for ele in strs:
            sorted_ele = self.count_sortingString(ele)
            if sorted_ele in frq:
                frq[sorted_ele].append(ele)
            else:
                frq[sorted_ele] = [ele]
        return frq


a1 = Solution()
res = a1.groupAnagrams(['act','cat','atc','car','rac','bat','tab','tac','top'])

print(list(res.values()))