class Solution
{ 
    public static int print2largest(int A[],int N) 
    {
        //CODE HERE
        int large=A[0];
        int seclarge=-1;
        
        for(int i=1;i<N;i++){
            if(A[i]>large){
                seclarge=large;
                large=A[i];
            }
            else if(A[i]>seclarge && A[i]!=large){
                seclarge=A[i];
            }
        }
        return seclarge;
    }
}