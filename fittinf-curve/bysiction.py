class Bysiction :
    coeffient_list :list
    start : int
    end : int
    decimals :int
    def __init__(self) -> None:
        """
        this is only for polynomials
        """
        pass
    def setequation(self, coeffient_list: list,start: int,end : int,decimals : int = 4) :
        """
        please enter the formula as list
        """
        self.decimals=decimals
        self.start=start
        self.end=end
        self.coeffient_list=coeffient_list
        self.eq_str: str=""
        self.counter=0
        def equation(n : int):
            self.eq_str+=f"{self.coeffient_list[self.counter]}X^{n}"
            self.counter+=1
            if self.counter==len(self.coeffient_list) :
                return
            self.eq_str+="+"
            equation(n-1)
        equation(len(self.coeffient_list)-1)
        print(self.eq_str)
    def _power(self,n:object,p:int) ->object:
        if p==0 :
            return 1
        return n*self._power(p=p-1,n=n)
    def get_f_of_x(self,c : int,test_point:int):
        global sum
        po=len(self.coeffient_list)-1
        if c==po :
            sum=0
        if c==-1 :
            return
        sum+=self.coeffient_list[po-c]*self._power(n=test_point,p=c)
        self.get_f_of_x(c-1,test_point)
        return sum
    def get_intervals(self) :
        mp={}
        """
        this method is created to generate [a,b] interval
        """
        self.count=self.start
        self.all_posible_roots_intervals=[]
        self.roots=[]
        def rec_func() ->dict:
            if self.count==self.end+1 :
                return
            x=self.get_f_of_x(len(self.coeffient_list)-1,self.count)
            self.count+=1
            if x * self.get_f_of_x(len(self.coeffient_list)-1,self.count) <0:
                self.all_posible_roots_intervals.append([self.count-1,self.count])
            if x==0 :
                self.roots.append(self.count-1)
            rec_func()
            mp['integer roots']=self.roots
            mp['intervals']=self.all_posible_roots_intervals
            return mp
        return rec_func()
    def calc_numerical_roots(self,intervals : list) :
        self.a=float(f"{intervals[0] : .{self.decimals}f}")
        self.b=float(f"{intervals[1] : .{self.decimals}f}")
        print("n            a               b              x            f(x)")
        mp=[]
        self.val=float(f"{0 : .{self.decimals}f}")
        self.x=float(f"{(self.a+self.b)/2 : .{self.decimals}f}")
        self.c=1
        def rec():
            self.x=float(f"{(self.a+self.b)/2 : .{self.decimals}f}")
            if self.val == float(f"{self.get_f_of_x(len(self.coeffient_list)-1,self.x): .{self.decimals}f}") :
                return self.x
            self.val=float(f"{self.get_f_of_x(len(self.coeffient_list)-1,self.x): .{self.decimals}f}")
            print(f"{self.c}",end=" ")
            print(f"          {self.a}",end=" ")
            print(f"            {self.b}",end=" ")
            print(f"           {self.x}",end=" ")
            print(f"          {self.val : .{self.decimals}f}",end=" ")
            print("\n")
            mp.append(self.c)
            if self.val * self.get_f_of_x(len(self.coeffient_list)-1,self.a) <0:
                self.b=self.x
            else :
                self.a=self.x
            self.c+=1
            rec()
            return self.x
        print(mp)
        return rec()
def main() :
    """
    Enter your code here\n
    Note : when you enter polynomial you must enter it as list for example
    X^2+4x-1=0 => [1,4,-1]
    """
    b=Bysiction()
    b.setequation([1,0,-8,5],start=-5,end=5,decimals=4)
    print(b.get_intervals())
    print(b.calc_numerical_roots([-4, -3]))
if __name__=="__main__" :
    main()