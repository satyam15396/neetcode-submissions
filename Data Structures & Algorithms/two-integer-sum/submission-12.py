class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using HashMap
        Map = {} 
        for index in range(len(nums)):
            if target - nums[index] in Map.keys():
                return [Map[target - nums[index]], index]
            Map[nums[index]] = index
        return []
