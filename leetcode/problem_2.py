class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        lis=[]
        for i in nums :
            if i>0 :
                lis.append(i)
        lis.sort()
        print(lis)
        for i in range(len(lis)) :
            if i==len(lis)-1 :
                break
            if(lis[i+1]-lis[i])>=2 :
                return lis[i]+1
            elif lis[i]-1<=0:
                return lis[i+1]+1
            else :
                return 1
        
