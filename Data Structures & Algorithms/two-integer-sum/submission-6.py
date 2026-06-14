class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using sorting and two pointes
        data = []
        for i,num in enumerate(nums):
            data.append([num,i])
        data = sorted(data)
        i,j = 0, len(nums)-1

        while i<j:
            if data[i][0] + data[j][0] == target:
                return sorted([data[i][1],data[j][1]])
            elif data[i][0] + data[j][0] > target:
                j-=1
            else:
                i+=1

        return []
