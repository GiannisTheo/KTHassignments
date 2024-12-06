import math as m
import sys
#limit = sys.getrecursionlimit()
sys.setrecursionlimit(200000)


def coins_with_table(n,a,b,c,coins):
    if n in coins:
        return coins[n]
    elif n<0: return m.inf
    else: 

        cc = 1 + coins_with_table(n-c,a,b,c,coins)
        
        cb = 1 + coins_with_table(n-b,a,b,c,coins)
        ca = 1 + coins_with_table(n-a,a,b,c,coins)
        coins[n] = min([n,ca,cb,cc])
        return coins[n]





if __name__ == '__main__':
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())

    coins = {0:0}
    answer = coins_with_table(n,a,b,c,coins)
    print(answer)