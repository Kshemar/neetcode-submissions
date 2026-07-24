class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        arr=[]
        for key, value in freq.items():
            arr.append([value,key])
        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res