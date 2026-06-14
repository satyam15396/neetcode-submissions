class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using HashMap
        Map = {}
        for i, num in enumerate(nums):
            diff = target- num
            if diff in Map.keys():
                return [Map[diff],i]
            Map[num] = i
            print(Map)
        return []