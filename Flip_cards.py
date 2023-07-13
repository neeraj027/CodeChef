t = int(input())
for i in range(t):
    N, X = map(int,input().split())
    if X==0 or X==N:
        print("0")
    elif X<=(N-X):
        print(X)
    elif (N-X)<X:
        print(N-X)
