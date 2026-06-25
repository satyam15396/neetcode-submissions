class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        lenOfList = len(nums)
        
        for i in range(lenOfList):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = lenOfList - 1
            
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                
                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    # Append the values, not the indices
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return answer