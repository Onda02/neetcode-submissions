class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = "abcdefghilmnopqrstuvz"
        s1_count = [0]* len(alphabet)
        s2_count = [0]* len(alphabet)

        for c in s:
            index = alphabet.find(c)
            s1_count[index]+=1
        for c in t:
            index = alphabet.find(c)
            s2_count[index]+=1
        
        return s1_count == s2_count