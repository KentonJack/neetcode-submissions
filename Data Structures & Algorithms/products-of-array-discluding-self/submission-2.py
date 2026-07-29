class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if set(nums) == {0}:
            return nums
        p = 1
        zero = 0
        for n in nums:
            if n != 0:
                p *= n
            else:
                zero += 1
        if zero > 1:
            return [0] * len(nums)
        pro = []
        for n in nums:
            if n != 0:
                if zero > 0:
                    pro.append(0)
                else:
                    pro.append(p // n)
            else:
                pro.append(p)
        return pro