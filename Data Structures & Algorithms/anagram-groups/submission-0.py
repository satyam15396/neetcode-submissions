class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #using hashmap and ascii value to create keys
        Map = defaultdict(list)
        for st in strs:
            key = [0]*26
            for i in st:
                key[ord(i)-ord('a')] += 1
            Map[tuple(key)].append(st)
        return list(Map.values())