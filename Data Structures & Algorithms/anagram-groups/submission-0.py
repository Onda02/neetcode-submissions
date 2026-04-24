class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortstr = []
        grouped = []
        list_to_be_appended = []
        used = set()
        for s in strs:
            sortstr.append(sorted(s))

        for i in range(len(sortstr)):
            if i in used:
                continue
            group = [strs[i]]
            for j in range(i+1, len(sortstr), 1):
                if (sortstr[i] == sortstr[j]):
                    group.append(strs[j])
                    used.add(j)
            grouped.append(group)
        
        return grouped
