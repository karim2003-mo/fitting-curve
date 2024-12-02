import numpy as np
import matplotlib.pyplot as plot
n=int(input("please enter the numper of measurements : "))
x=[]
for i in range(n) :
    varx=int(input("X : "))
    vary=int(input("Y : "))
    x.append((varx,vary))
print(x)
print(tuple(x[0])[1])
array=np.array(ndmin=2,object=[],dtype=np)
def sumlist(l) ->int :
    num=0
    for i in l :
        num+=i
    return num
# index is refers to column for example index =0 refers to sumx ,index=1 refers to sumy,index=2 refers to sum_x_square,index=3 refers to sum_xy
def arrange(l,index)->list :
    arranged_list=[]
    total_list=[]
    if index<2 :
        for i in l :
            arranged_list.append(i[index])
    elif index ==2 :
        for i in l :
            arranged_list.append(i[0]*i[0])
    else :
        for i in l :
            arranged_list.append(i[0]*i[1])
    total_list.extend(arranged_list)
    total_list.append(sumlist(arranged_list))
    return total_list
array=np.array([arrange(x,0)])
for i in range(4) :
    if i==3 :
        break
    array = np.vstack((array,arrange(x,i+1)))
print(array.ndim)
print(array[2])
sumx=array[0][n]
sumy=array[1][n]
sum_x_square=array[2][n]
sum_xy=array[3][n]
# y= aX + b
b=((sum_xy*sumx)-(sum_x_square*sumy))/((sumx*sumx)-(n*sum_x_square))
a=(sumy-(n*b))/sumx
print(f"th eq is Y = {a}X+{b}")
x = np.linspace(-10, 10, 400)
y = a*x + b
plot.plot(x, y, label=f'$y = {a}x + {b}$')
plot.title(f'Graph of $y = {a}x + {b}$', fontsize=16)
plot.xlabel('x', fontsize=14)
plot.ylabel('y', fontsize=14)

plot.grid(True)
plot.legend()
plot.show()