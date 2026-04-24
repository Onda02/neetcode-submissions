class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_find =set()
        for n in nums:
            if(n in num_find):
                return True
            num_find.add(n)
        return False


        