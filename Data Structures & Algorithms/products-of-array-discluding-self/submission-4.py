class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        print(n)
        prefix = [1]*n
        suffix = [1]*n

        result = [1]*n

        for i in range(n):
            if i > 0:
                prefix[i] = nums[i]*prefix[i-1]
            else:
                prefix[i] = nums[i]
            
        for i in reversed(range(n)):
            if i < n -1 :
                suffix[i] = nums[i] * suffix[i+1]
            else:
                suffix[i] = nums[i]

        for i in range(n):
            if i>0 and i<n -1:
                result[i] = prefix[i-1] * suffix[i+1]
            elif i==0:
                result[i] = suffix[i+1]
            elif i==n-1:
                result[i] = prefix[i-1]
        return result
