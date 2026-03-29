class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Brute force method:
        target - number = number in the list

        hashmap, which will hold the target - number as key and value as the index
        '''

        dic = {}
        diff = 0
        for i, j in enumerate(numbers):
            if j in dic:
                return [dic[j], i+1]
            
            else:
                diff = target - j
                dic[diff] = i+1


