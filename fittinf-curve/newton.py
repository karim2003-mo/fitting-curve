# this code calc Newton forward
class Newton :
    X_readings : list
    Y_readings : list
    num_d :int 
    s_val : object
    step : object
    req_val :object
    table_data={}
    def __init__(self,X_readings,Y_readings,req_val) -> None:
        """
        The X Readings must have the same step difference
        """
        self.req_val=req_val
        self.X_readings=X_readings
        self.Y_readings=Y_readings
        self.num_d=len(self.X_readings)-1
        self._newten_table()
        self.calc_s()
    # dy=(yn+1)-(yn-1)
    def _newten_table(self)-> dict:
        """
        this is method generate full newton table
        """
        self.table_data['X']=self.X_readings
        self.table_data['Y']=self.Y_readings
        self.rec_list=self.Y_readings
        def recursive():
            l=[]
            for i in range(self.num_d):
                l.append(self.rec_list[i+1]-self.rec_list[i])
                if i==self.num_d-1 :
                    break
            self.table_data[f'dy{self.num_d}']=l
            self.rec_list=l
            self.num_d-=1
            if self.num_d==0:
                return
            recursive()
        recursive()
        return self.table_data
    def calc_h(self)->bool:
        x=self.X_readings[1]-self.X_readings[0]
        c=0
        for i in self.X_readings :
            c+=1
            if c==len(self.X_readings):
                break
            if x/(self.X_readings[self.X_readings.index(i)+1]-i) < 0.999996 or x/(self.X_readings[self.X_readings.index(i)+1]-i)>1.0000008:
                return False
            x=self.X_readings[self.X_readings.index(i)+1]-i
        self.step=x
        return True
    def calc_s(self):
        """
        this is method calc s variable
        """
        if self.calc_h()==False:
            return None
        else :
            print("fasgtshgdfhd")
            x0=self.X_readings[0]
            self.s_val=(self.req_val-x0)/self.step
            return (self.req_val-x0)/self.step
    def final_output(self):
        """
        this method give the value of formula at any point
        """
        l=[self.Y_readings[0]]
        values=list(self.table_data.values())
        self.n=1
        self.varx=self.s_val
        def rec_output(i : int)-> object:
            if i ==1 :
                return self.varx
            self.varx*=(self.s_val-self.n)
            if self.n==i-1 :
                self.n+=1
                return self.varx
            else :
                self.n+=1
                rec_output(i)
        def fact(n) -> int:
            if n<=1 :
                return 1
            return n*fact(n-1)
        def sum(l:list):
            x=0
            for m in l :
                x+=m
            return x
        for i in values[2:]:
            var=rec_output(len(self.Y_readings)-len(i))/fact(len(self.Y_readings)-len(i))
            l.append(i[0]*var)
            print(l)
        print(self.table_data.values())
        print(l)
        return sum(l)
n=Newton(X_readings=[1.0,1.2,1.4,1.6,1.8],Y_readings=[1.0000,1.0910,1.1609,1.2311,1.3612],req_val=1.5)
print(n.final_output())
