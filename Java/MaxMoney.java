class Solution {
    static int maximizeMoney(int N , int K) {
        // code here
        // if(N<=2){
        //     return K;
        // }
        // int tofind=0;
        if(N%2==0){
            return (N/2)*K;
        }
        else{
            return ((N/2)+1) * K;
        }
        
        // return tofind*K;
    }
};