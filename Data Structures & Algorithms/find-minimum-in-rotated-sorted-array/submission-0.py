class Solution:
    def findMin(self, nums: List[int]) -> int:
        val=nums[0]
        for i in range(1,len(nums)):
            val= min(val, nums[i])
        return val