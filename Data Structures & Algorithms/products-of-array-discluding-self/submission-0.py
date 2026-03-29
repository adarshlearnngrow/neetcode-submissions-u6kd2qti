class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force logic
        final_list = []
        for i in range(len(nums)):
            calc = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else: 
                    calc *= nums[j]
            final_list.append(calc)

        return final_list        
        


        