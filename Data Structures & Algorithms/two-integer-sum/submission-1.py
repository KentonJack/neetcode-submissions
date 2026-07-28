class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            d[target - n] = i
        for i,n in enumerate(nums):
            if n in d and d[n] != i:
                return [min(d[n], i), max(d[n], i)]