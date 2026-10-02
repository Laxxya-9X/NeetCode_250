def isAnagram(s,t):
    m = len(s)
    n = len(t)
    dic = {}
    if m != n:
        return False
    for ele in s:
        if ele in dic :
            dic[ele] += 1
        else :
            dic[ele] = 1
    for ele in t:
        if ele in dic  and dic[ele]>0:
            dic[ele]-=1
        else:
            return False
    return True
print("Checking string is anagram or not ========>>>>>")
s = input("Enter first string : ")
t = input("Enter second string : ")
res = isAnagram(s,t)
print(res)