class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortstr = {}
        for s in strs:
            key = "".join(sorted(s)) 
            if key in sortstr:
                sortstr[key].append(s)
            else:
                sortstr[key] = [s]
      
        return list(sortstr.values())

