class Solution:

    def __init__(self):
        self.size = 11
        self.Bucket = [[] for _ in range(self.size)]

    def _hash(self,k):
        return k % self.size

    def add(self,k):
        indx = self._hash(k)
        if k not in self.Bucket[indx]:
            self.Bucket[indx].append(k)

    def remove(self,k):
        indx = self._hash(k)
        if k in self.Bucket[indx]:
            self.Bucket[indx].remove(k)
    
    def contains(self,k):
        indx = self._hash(k)
        return k in self.Bucket[indx]



s = Solution()
s.add(1)
s.add(2)
s.add(5)
s.add(5)
s.add(9)


print(s.Bucket)
res = s.contains(5)
print(res)
s.remove(5)
print(s.Bucket)