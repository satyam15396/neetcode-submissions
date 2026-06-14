class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        pre = 1
        for i in range(len(nums)):
            pre = pre * nums[i]
            prefix.append(pre)
        
        post = 1
        for i in range(len(nums)-1,-1,-1):
            post = post * nums[i]
            postfix.insert(0,post)

        res = []
        for i in range(len(nums)):
            if i==0:
                res.append(postfix[i +1])
            elif i == len(nums) -1:
                res.append(prefix[i-1]) 
            else:
                res.append(prefix[i-1] * postfix[i +1]) 

        return res          





