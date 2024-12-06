import math as m



def coins(n,a,b,c):
    if n<0: return m.inf
    elif n==0: return 0
    else:
        ca = coins(n-a,a,b,c)+1
        cb = coins(n-b,a,b,c)+1
        cc = coins(n-c,a,b,c)+1
        return min([n,ca,cb,cc])


if __name__ == "__main__":
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    answer = coins(n,a,b,c)
    print(answer)
    