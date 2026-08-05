class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]
        maxq = [-s for s in stones]
        heapq.heapify(maxq)
        while len(maxq) > 1:
            fir = heapq.heappop(maxq)
            sec = heapq.heappop(maxq)
            if sec > fir:
                heapq.heappush(maxq, fir - sec)
        maxq.append(0)
        return abs(maxq[0])