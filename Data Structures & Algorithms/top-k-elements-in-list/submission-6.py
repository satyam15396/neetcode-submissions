class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using HashMap and Array
        Map = {}
        for num in nums:
            Map[num] = 1 + Map.get(num, 0)
        
        array = []
        for key,val in Map.items():
            array.append([val,key])
        array.sort()
        
        res = []
        while len(res) < k :
            res.append(array.pop()[1])
        return res
