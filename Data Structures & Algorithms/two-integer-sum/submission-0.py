class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        o1 = -1
        o2 = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    o1 = i
                    o2 = j
        return [o1, o2]