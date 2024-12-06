



def solve(n,k,p):
    g = [0]*(n+1)
    for i in range(1,n+1):
        if i<k: g[i] = 0
        elif i==k: g[i]= p**k
        else:
            g[i] = g[i-1]+(p**k)*(1-p)*(1-g[i-k-1])
    
    return g[n]


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = float(input())

    answer = solve(n,k,p)
    print(answer)

