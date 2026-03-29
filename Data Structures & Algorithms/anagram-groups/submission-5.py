class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rec = {}
        for i in strs:
            sort_str = tuple(sorted(i))
            if sort_str in rec.keys():
                rec[sort_str].append(i) 
            else:
                rec[sort_str] = [i]

        return list(rec.values())