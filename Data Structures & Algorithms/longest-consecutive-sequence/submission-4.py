class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        eg: [3,2, 10, 11, 12]
        [2: 1, 10: 2]


        
        '''
        
        # start sequence
        start_sequence = []
        nums = set(nums)
     
        for i in nums:
            if (i - 1) not in nums:
                start_sequence.append(i)
            

        max_count = 0        
        for i in start_sequence:
            count = 0
            
            while i in nums:
                count += 1 
                i = i+1
            max_count = max(count, max_count)

        return max_count
            

            

        
                
            


        
       
                

