class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        s, e = intervals[0]
        merged = []

        for i in range(len(intervals)):
            ns, ne = intervals[i]
            if ns <= e:
                e = max(e, ne)
            else:
                merged.append([s, e])
                s, e = ns, ne
        merged.append([s, e])
        return merged