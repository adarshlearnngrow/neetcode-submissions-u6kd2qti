class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean the data
        
        # s = ''.join(s.split(" "))
        final_s = ''
        for i in s.lower():
            # print(i)
            if not(i.isnumeric() or i.isalpha()):
                continue
            
            final_s += i
            
        # print("HII")

        if final_s == final_s[::-1]:
            return True
        return False