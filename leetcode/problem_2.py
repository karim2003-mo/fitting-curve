class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        lis=[]
        for i in nums :
            if i>0 :
                lis.append(i)
        lis.sort()
        print(lis)
        if len(lis)>1:
            if lis[0]==1:
                for i in range(len(lis)) :
                    print(i)
                    if i==len(lis)-1 :
                        return lis[len(lis)-1]+1
                    if(lis[i+1]-lis[i])>=2 :
                        return lis[i]+1
            else :
                return 1
        elif len(lis)==1 :
            if lis[0]-1>=1:
                return 1
            else :
                return 2
        return 1
s=Solution()
print(s.firstMissingPositive([1,2,0]))
