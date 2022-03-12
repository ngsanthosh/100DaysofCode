class Solution {
    int remove_duplicate(int A[],int N){
        // code here
        int j=0;
        
        for (int i=0;i<N;i++){
            if( A[j] != A[i] ){
                j++;
                A[j]=A[i];
            }
                
        }
        return j+1;
    }
}