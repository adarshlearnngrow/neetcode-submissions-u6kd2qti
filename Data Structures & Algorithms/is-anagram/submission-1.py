class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Case 1: if len is not same
        if len(s) != len(t):
            return False
        
        '''
        Case 2: when len is same, we will have two hashmap and have the count of each character
        then in the end we can compare
        Time complexity is two loop, not nested, so O(n+m)
        Space complextiy for two hash the worst it can get is O(52), then you simplify
        O(1)
        O(52)    → constant, never grows
        O(1)     → constant, never grows

        They're the SAME thing!
        '''
        s_count = {}
        t_count = {}

        for i in s:
            if i in s_count.keys():
                s_count[i] += 1
            else:
                s_count[i] = 1

        for i in t:
            if i in t_count.keys():
                t_count[i] += 1
            else:
                t_count[i] = 1

       
        return s_count == t_count
        
        