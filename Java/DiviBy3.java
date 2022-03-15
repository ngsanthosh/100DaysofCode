// https://practice.geeksforgeeks.org/problems/form-a-number-divisible-by-3-using-array-digits0717/1#

class Solution {
    static int isPossible(int N, int arr[]) {
        // code here
        int sum=0;
        for(int i=0;i<N;i++){
            int mod=arr[i]%3;
            sum+=mod;
        }
        return sum%3==0 ? 1 : 0;
    }
}