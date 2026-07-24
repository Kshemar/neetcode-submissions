class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums= [*nums1, *nums2]
        nums.sort()
        l, r= 0, len(nums)-1
        res=0
        m=(l+r)//2
        if len(nums)%2==1:
            res= nums[m]
        else:
            res= (nums[m]+nums[m+1])/2
        return res