class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        n = len(nums)
        for num in nums:
            if num == 0:
                zeros +=1
                if zeros > 1:
                    return [0]*n

        zero_index = nums.index(0) if zeros == 1 else []
        if zero_index != []:
            nums.remove(0)

        prod = math.prod(nums)
        if zeros == 1:
            res = [0]*n
            res[zero_index] = prod
        else:
            res = []
            for num in nums:
                res.append(int(prod/num))
        return res



