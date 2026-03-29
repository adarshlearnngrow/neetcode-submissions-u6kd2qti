class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force logic
        # final_list = []
        # for i in range(len(nums)):
        #     calc = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else: 
        #             calc *= nums[j]
        #     final_list.append(calc)

        # return final_list      

    
        left = [1]
        for i in range(1, len(nums)):
           
            prod = nums[i-1] * left[i-1]
            left.append(prod)

                # prod2 = nums[i+1:] 
        # return left

        right = [1] * (len(nums))
        for i in range(len(nums)-2,-1,-1):
            prod = nums[i+1] * right[i+1]
            right[i]=(prod)
        # return right
        final=[]
        for i in range(len(nums)):
            final.append(left[i]*right[i])
        return final






























 










            

        


        