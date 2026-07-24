class MedianFinder:

    def __init__(self):
        self.arr= []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        median = 0
        n= len(self.arr)
        if n%2 !=0:
            median = self.arr[n//2]
        else:
            median = (self.arr[n//2]+ self.arr[n//2 -1])/2
        return median