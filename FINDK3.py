T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    if (X*Y)%Z==0:
        A=X*Y
        B=Z
        print(A,B)
    elif (Y*Z)%X==0:
        A=Y*Z
        B=X
        print(A,B)
    elif (X*Z)%Y==0:
        A=X*Z
        B=Y
        print(A,B)
    else :
        print("-1")
