import math as m

def coins_bu(n,a,b,c):
    coins = [0]*(n+1) # [0 for i in range(n+1)]
    for i in range(1,n+1):
        if i-a<0: ca = m.inf
        else: ca = 1 + coins[i-a]

        if i-b<0: cb=m.inf
        else: cb = 1+coins[i-b]

        if i-c<0: cc=m.inf
        else: cc = 1+coins[i-c]

        coins[i] = min([i,ca,cb,cc])
    return coins[n]


if __name__ == "__main__":
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())

    answer = coins_bu(n,a,b,c)
    print(answer)
    