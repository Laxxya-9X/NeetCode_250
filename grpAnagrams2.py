word = ['cat','act','tac','bat','car']
def groupAnagrams(strs):

        freq = {}

        for ele in strs: # act
            # count = [0]*26
            key = "".join(sorted(ele))   #inbuilt method used
                # count[ord(ch)-ord('a')]+=1 #no inbuilt function used

            # key = tuple(count)   


            if key in freq:
                freq[key].append(ele)
            else:
                freq[key] = [ele] 
        return list(freq.values())

print(groupAnagrams(word))

