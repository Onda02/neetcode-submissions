class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string))+'#'+string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j]!="#":
                j=j+1
            length = int(s[i:j])
            start = j+1
            end = start+length
            decoded.append(s[start:end])
            i = end
            

        return decoded