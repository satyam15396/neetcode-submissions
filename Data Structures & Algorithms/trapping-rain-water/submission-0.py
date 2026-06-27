class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        lenOfInput = len(height)
        trappedWater = 0
        prefix = [0]
        suffix = [0]

        for h in range(1,lenOfInput):
            prefix.append(max(height[h-1],prefix[h-1]))
        
        for h in range(lenOfInput-2,-1,-1):
            suffix.insert(0,max(height[h+1],suffix[0]))
        
        for h in range(lenOfInput):
            currWater = min(prefix[h], suffix[h]) - height[h]
            if currWater > 0:
                trappedWater += currWater
        return trappedWater
            
