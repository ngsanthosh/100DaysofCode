class Solution
{
    //Function to return the largest possible number of n digits
    //with sum equal to given sum.
    static String largestNumber(int n, int sum)
    {
        // add your code here
        int bal=0;
        if(sum>(n*9)){
            return "-1";
        }
        if(sum==(n*9)){
            return "9".repeat(n);
        }
        String res = "";
        while (n!=0){
            if(sum>=9){
                res+="9";
            }
            else{
                res+=sum;
            }
            sum=sum-9;
            if(sum<0) sum=0;
            // bal=s
            n--;
        }
        return res;
    }
}