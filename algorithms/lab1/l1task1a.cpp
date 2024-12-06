#include <iostream>
#include <bits/stdc++.h>
#include <vector>
#include <algorithm>

using namespace std;




int coins(int n,int a,int b, int c){
    int ca,cb,cc;
    if (n<0) return INT_MAX-1;
    else if (n==0) return 0;
    else {
        ca = coins(n-a,a,b,c)+1;
        cb = coins(n-b,a,b,c)+1;
        cc = coins(n-c,a,b,c)+1;
        return min(n,min(ca,min(cb,cc)));

    }

}


int coins_with_table(int n, int a , int b , int c){
    int ca,cb,cc;
    vactor<int> coins(n+1,0);
    if (n<0) return INT_MAX-1;
    else if (n==0) 
}


int solve(int n,int a, int b, int c){
    vector<int> coins(n+1,0);
    int ca,cb,cc;
    for (int i = 1; i<n+1; i++){


        if (i-a<0) ca = INT_MAX;
        else ca = 1+ coins[i-a];

        if (i-b<0) cb = INT_MAX;
        else cb = 1+ coins[i-b]; 

        if (i-c<0) cc = INT_MAX;
        else cc = 1 + coins[i-c];



        coins[i] = min(i,min(ca,min(cb,cc)));
    }
    return coins[n];



}



int main(){
    int n,a,b,c;
    cin >> n >> a >> b >> c;
    
    //int result = coins(n,a,b,c);
    int result = solve(n,a,b,c);
    cout << result << endl;
    return 0;

}


