class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0]= 1 #only one way sum of 0 elements is 0

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur, count in dp.items():
                next_dp[cur + nums[i]] += count
                next_dp[cur - nums[i]] +=count
            dp = next_dp
        return dp[target]