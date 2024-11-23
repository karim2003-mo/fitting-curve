# this code is for generate lagrange equation
import numpy as np
try :
    num_readings=int(input("Enter the number of readings : "))
except :
    print("invalid input")
arr_readings=np.empty(num_readings,dtype=object)
for i in range(num_readings) :
    x=int(input(f"X{i} : "))
    y=int(input(f"Y{i} : "))
    arr_readings[i]=(x,y)
num_terms=num_readings
p_arr=np.empty(num_readings)
terms = np.empty(num_readings, dtype=object)
def multiple(j : int,k : int) :
    if k==j :
        k=k-1
    if k<0:
        return 1
    else:
        if k!=j :
            return (arr_readings[j][0]-arr_readings[k][0])*multiple(j,k-1)
def str_terms(j,n):
    if j==n :
        n=n+1
    if n>= num_terms :
        return 1
    return f"(X-{arr_readings[n][0]}){str_terms(j,n+1)}"
terms_as_int=np.empty(num_terms,dtype=object)
for i in range(num_readings):
    p_arr[i]=arr_readings[i][1]/multiple(i,num_readings-1)
    terms[i]=str_terms(i,0)[0:len(str_terms(i,0))-1]
def final_eq(n):
    if n>=num_terms :
        return 1
    return f"{p_arr[n]}*{terms[n]}+{final_eq(n+1)}"
print(f"L(X) = {final_eq(0)[0:len(final_eq(0))-2]}")
calcing=str(input("do you want to calc any value Y/N ?"))
if calcing.lower()=="y" :
    b=True
    while b :
        val=int(input("Enter the value :"))
        def terms_as_integer(j,n,value):
            if j==n :
                n=n+1
            if n>= num_terms :
                return 1
            return (value-arr_readings[n][0])*terms_as_integer(j,n+1,value)
        for i in range(num_readings) :
            terms_as_int[i]=terms_as_integer(i,0,val)
        f=0
        c=0
        def final_num():
            global f,c
            if c==len(p_arr) :
                return f
            f=f+(p_arr[c]*terms_as_int[c])
            c+=1
            final_num()
        final_num()
        print(f"L({val}) = {f}")
        another_val=str(input("do you want to calc another value Y/N ?"))
        if another_val.lower()=="y" :
            pass
        else :
            b=False