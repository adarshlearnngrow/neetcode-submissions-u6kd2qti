class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, j in enumerate(nums):
            diff = target - j
            if j in dic.keys():
                return [dic[j], i]
            dic[diff] = i

        