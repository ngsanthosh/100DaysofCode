class Solution{
    static boolean isPrime(int p){
        // if(p<=1){
        //     return false;
        // }
        // for(int i=2;i<=p;i++){
        //     if(p%i==0){
        //         return false;
        //     }
        // }
        // return true;
        if(p==2||p==3||p==5||p==7){
            return true;
        }
        return false;
    }
    static int primeSum(int N){
        // code here
        int sum=0;
        while (N!=0){
            int s=N%10;
            if(isPrime(s)){
                sum+=s;
            }
            N=N/10;
        }
        return sum;
    }
}