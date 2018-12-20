#More About Iteration Section 3
#Tatum Gray
#3/31/2016

def multitable(n,m):
    print("* |",end="")
    for m in range(1,m+1):
        print("",m,"",end="")
    print()
    print("-"*2 + "+" + "-"*3*m)
    for n in range(1,n+1):
        print(n,"|",end="")
        print('',n*m)
multitable(4,5)
