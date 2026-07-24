class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        if not nums:
            return 0
        nums.sort()
        cur=nums[0]
        streak=0
        i=0
        while i<len(nums):
            if cur!=nums[i]:
                cur=nums[i]
                streak=0
            while i<len(nums) and nums[i]==cur:
                i+=1
            streak+=1
            cur+=1
            count=max(count, streak)
        return count