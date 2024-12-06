import math as m
import sys
from matplotlib import pyplot as plt
from time import time
#limit = sys.getrecursionlimit()
sys.setrecursionlimit(20000000)


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


def plot_simulations(times1,times2,ns,n2s):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Time complexity of recursive solution')
    ax1.plot(ns,times1)
    ax2.plot(n2s,times2)
    plt.show()


if __name__ =="__main__":
    a = 5
    b = 6
    c = 7
   
    # n = n+1
    n=0
    ns =[]
    times = []
    print("incrementing by one experiment.....")
    while(n!=1024):
        start = time()
        coins = {0:0}
        answer = coins_with_table(n,a,b,c,coins)
        end = time()
        times.append(end-start)
        ns.append(n)
        if n%1000==0:
            print("done n ={} in {} sec".format(n,end-start))
        if end-start>1: break
        n+=1
    
    print("First experiment done")
    #n = 2*n
    times2 = []
    n2 = 1
    n2s = []
    print("doubling n experiment.....")
    while(n2!=2048):
        start = time()
        coins = {0:0}
        answer = coins_with_table(n2,a,b,c,coins)
        end = time()
         
        times2.append(end-start)
        n2s.append(n2)
        if n%1000==0:
            print("done n ={} in {} sec".format(n2,end-start))
        if end-start>1:
            break
        n2 = n2*2
          
    print('done doubling n experiment')


    tart = time()
    coins = {0:0}
    n=1000000
    answer = coins_with_table(n,a,b,c,coins)
    end = time()
    print("done n={} in {} sec".format(n,end-start))

    #find maximum n for runtime 1 sec
    
    # plot_times(times,n)
    plot_simulations(times,times2,ns,n2s)