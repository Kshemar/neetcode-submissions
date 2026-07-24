class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list= [1] * len(nums)
        postfix=1
        prefix = 1
        for i in range(len(nums)):
            list[i] = prefix
            prefix *= nums[i]
        for j in range(len(nums)-1,-1,-1):
            list[j]*=postfix
            postfix*=nums[j]
        return list
