class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using HashMap and Array
        counter = Counter(nums)

        mem = [0]*(len(nums)+1)
        for num, freq in counter.items():
            if mem[freq] == 0:
                mem[freq] = [num]  
            else:
                mem[freq].append(num)

        res = []
        for i in range(len(nums),0,-1):
            if mem[i] != 0:
                res.extend(mem[i])
            if len(res) == k:
                return res
            
        
        