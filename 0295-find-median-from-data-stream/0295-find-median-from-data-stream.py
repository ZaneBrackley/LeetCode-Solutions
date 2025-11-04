import heapq

class MedianFinder(object):

    def __init__(self):
        self.lowerHalf = []
        self.upperHalf = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.lowerHalf, -num)

        heapq.heappush(self.upperHalf, -heapq.heappop(self.lowerHalf))

        if len(self.upperHalf) > len(self.lowerHalf):
            heapq.heappush(self.lowerHalf, -heapq.heappop(self.upperHalf))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lowerHalf) > len(self.upperHalf):
            return -self.lowerHalf[0]
        return (-self.lowerHalf[0] + self.upperHalf[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()