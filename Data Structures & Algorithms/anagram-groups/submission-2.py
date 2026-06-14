class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #using hashmap and ascii value to create keys
        Map = {}
        for st in strs:
            key = [0]*26
            for i in st:
                key[ord(i)-ord('a')] += 1
            key = tuple(key)
            if key in Map.keys():
                Map[key].append(st)
            else:
                Map[key] = [st]
        return list(Map.values())