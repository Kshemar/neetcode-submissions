class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        inp=set()
        l=0
        longest=0
        for r in range(len(s)):
            while s[r] in inp:
                inp.remove(s[l])
                l+=1
            inp.add(s[r])
            longest = max(longest, r-l+1)
        return longest