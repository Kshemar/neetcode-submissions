class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        Area=0
        stack= []
        for i,h in enumerate(heights):
            start =i
            while stack and stack[-1][1]> h:
                index, height= stack.pop()
                Area = max(Area, height * (i- index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            Area = max(Area, h* (len(heights)-i))
        return Area