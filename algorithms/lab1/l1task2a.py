import numpy as np



def solve(n,k,p):
    #print("starting to solve")
    f = np.zeros((n+1,k+1))
    f[:,0] = 1
    #print(f)
    for i in range(1,n+1):
        for j in range(1,k+1):
            f[i,j] = p*f[i-1,j-1] + (1-p)*f[i-1,k]
    return f[n,k]





if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = float(input())


    answer = solve(n,k,p)

    print(answer)




