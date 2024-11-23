l=[7,2,3,4,5,6]
lq=[]
k=1
def test(n: int) -> int:
    global k
    if n==0 :
        return 1
    return (l[0]-l[n])*test(n-1)
print(test(5))