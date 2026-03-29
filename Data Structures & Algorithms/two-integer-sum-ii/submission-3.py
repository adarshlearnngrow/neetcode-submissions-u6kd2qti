class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Brute force method:
        target - number = number in the list

        hashmap, which will hold the target - number as key and value as the index

        '''

        # dic = {}
        # diff = 0
        # for i, j in enumerate(numbers):
        #     if j in dic:
        #         return [dic[j], i+1]
            
        #     else:
        #         diff = target - j
        #         dic[diff] = i+1

        '''
        the array is sorted, so we could use soemthing in two pointers
        we cant imporve time complexitiy but we can imprve space complexitiy


        cases: [1 ,2,3,4] target = 6
        5 < 6
        '''
      

        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left +=1
            else:
                return[left+1,right+1]

        

            


                
            
            


        


