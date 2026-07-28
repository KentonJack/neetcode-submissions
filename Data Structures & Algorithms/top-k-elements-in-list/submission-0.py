class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        for i,v in c.items():
            heapq.heappush(h, (-v, i))
        topk = []
        for _ in range(min(len(h), k)):
            _, i = heapq.heappop(h)
            topk.append(i)
        return topk