class Solution :
    def increasingTriplet(self,l)->bool :
        c=0
        for i in range(len(l)) :
            if i==len(l)-1 :
                return False
        
            if (int(l[i])<int(l[i+1])):
                c+=1
            else:
                c=0
            if c>=2 :
                return True
        return False