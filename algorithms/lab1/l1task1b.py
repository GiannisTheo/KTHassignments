import math as m
from time import time
from matplotlib import pyplot as plt


def coins(n,a,b,c):
    if n<0: return m.inf
    elif n==0: return 0
    else:
        ca = coins(n-a,a,b,c)+1
        cb = coins(n-b,a,b,c)+1
        cc = coins(n-c,a,b,c)+1
        return min([n,ca,cb,cc])


def plot_times(times,n):
    ns = [2**i for i in range(n+1)]
    f = plt.figure()
    plt.plot(ns,times)
    plt.xlabel("n")
    plt.ylabel("time")
    plt.show()

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
    while(1):
        start = time()
        answer = coins(n,a,b,c)
        end = time()
        times.append(end-start)
        ns.append(n)
        if end-start>1: break
        n+=1
    
    print(" done calculating 1")
    #n = 2*n
    times2 = []
    n2 = 1
    n2s = []
    while(n2!=128):
        start = time()
        answer = coins(n2,a,b,c)
        end = time()
         
        times2.append(end-start)
        n2s.append(n2)
        print("done ",n2,end-start)
        if end-start>1:
            break
        n2 = n2*2
          
    print('done calculating 2')

    
    # plot_times(times,n)
    plot_simulations(times,times2,ns,n2s)
