from bysiction import Bysiction
class Newton_Raphson(Bysiction) :
    new_x=None
    Maximum_iteration=100
    def __init__(self) -> None:
        """
        this is only for polynomials
        """
        super().__init__()
    def test(self) :
        super().get_f_of_x()
    def diff1(self) :
        l=[]
        for i in range(len(self.coeffient_list)) :
            if i== len(self.coeffient_list)-1 :
                break
            x=self.coeffient_list[i]*(len(self.coeffient_list)-1-i)
            l.append(x)
        return l
    def get_diff1_val(self, val) :
        v=0
        for i in range(len(self.coeffient_list)) :
            if i== len(self.coeffient_list)-1 :
                break
            x=self.coeffient_list[i]*(len(self.coeffient_list)-1-i)
            v+=x*self._power(n=val,p=len(self.coeffient_list)-2-i)
        return v
    def diff2(self) :
        l=[]
        for i in range(len(self.diff1())) :
            if i== len(self.diff1())-1 :
                break
            x=self.diff1()[i]*(len(self.diff1())-1-i)
            l.append(x)
        return l
    def get_diff2_val(self, val) :
        v=0
        for i in range(len(self.diff1())) :
            if i== len(self.diff1())-1 :
                break
            x=self.diff1()[i]*(len(self.diff1())-1-i)
            v+=x*self._power(n=val,p=len(self.diff1())-2-i)
        return v
    def check_convergence(self,val) -> str:
        conv= abs((self.get_f_of_x(c=len(self.coeffient_list)-1,test_point=val)*self.get_diff2_val(val))/self._power(n=self.get_diff1_val(val),p=2))
        if conv<1 :
            return f"the convergance is equal to {conv} ,so that {val} is valid"
        else :
            return f"the convergance is equal to {conv} ,so that{val} is not valid"
    def calc_newton_val(self,val,num_of_decimals: int) :
        self.Maximum_iteration-=1
        if self.Maximum_iteration==0 :
            return
        print(val)
        q=float(f"{val-(self.get_f_of_x(c=len(self.coeffient_list)-1,test_point=val)/self.get_diff1_val(val)) : .{num_of_decimals}f}")
        print(q)
        if q==self.new_x :
            return
        self.new_x=float(f"{q: .{num_of_decimals}f}")
        self.calc_newton_val(val=q,num_of_decimals= num_of_decimals)
        return self.new_x
def main() :
    """
    Enter your code here
    """
    
if __name__=="__main__" :
    main()