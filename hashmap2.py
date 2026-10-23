class HashMap:
    def __init__(self):
        self.Bucket = [False] * 1000001


    def add(self,k):
        self.Bucket[k] = True

    def remove(self,k):
        self.Bucket[k] = False

    def contains(self,k):
        return self.Bucket[k]



obj = HashMap()
obj.add(5)
res = obj.contains(5)
print(res)
obj.remove(5)

