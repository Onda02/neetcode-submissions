class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count= {}
        for n in nums:
            if n in num_count:
                num_count[n]+=1
            else:
                num_count[n] = 1
        num_sort = sorted(num_count.items(), key = lambda x: x[1], reverse = True)
        result = [t[0] for t in num_sort]
        return result[:k]
