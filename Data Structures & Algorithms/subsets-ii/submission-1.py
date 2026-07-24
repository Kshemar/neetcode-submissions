class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n= len(nums)
        def backtrack(i, cur):
            if i == n:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            backtrack(i+1, cur)
            cur.pop()
            while i+1 < n and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1, cur)
            
        backtrack(0, [])
        return res


         