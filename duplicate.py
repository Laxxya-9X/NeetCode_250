arr = [1,2,3,6,3]
def isDulicate(arr):

    s =set()
    for i, ele in enumerate(arr):
        if ele in s:
            return f"Duplicacte element {ele} found at index {i}"
        s.add(ele)
    return False
print(isDulicate(arr))