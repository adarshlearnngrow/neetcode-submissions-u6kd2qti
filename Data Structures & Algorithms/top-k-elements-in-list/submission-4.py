class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        bucket = [[] for _ in range(len(nums)+1)]
        # frequency diagram
        for i in nums:
            if i not in counter.keys():
                counter[i] = 1
            else:
                counter[i] += 1
        print(counter)
        for i, j in counter.items():
          
            bucket[j].append(i)
        print(bucket)

        final = []
        
        for i in range(len(bucket) -1, -1, -1):
            if len(final) == k:
                return final
            else:
                final.extend(bucket[i])
        print(final)
        return []