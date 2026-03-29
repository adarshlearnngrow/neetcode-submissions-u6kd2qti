class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Logic 1
        # if len(nums) > len(set(nums)):
        #     return True
        # return False

        # logic 2
        a = set()
        for i in nums:
            if i in a:
                return True
            else:
                a.add(i)

        return False