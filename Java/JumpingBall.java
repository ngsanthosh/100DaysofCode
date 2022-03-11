// https://practice.geeksforgeeks.org/problems/jumpy-ball1449/1#

class Solution{
    static long jumpyBall(long N){
        // code here
        long add=0;
        while(N!=0){
            add=add+N;
            N=N/2;
        }
        return add*2;
    }
}