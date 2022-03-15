class Solution
{
    public String is_palindrome(int n)
    {
        // Code here
        int check=0;
        int check2=n;
        while (n!=0){
            int get=n%10;
            check=(check*10)+get;
            n=n/10;
        }
        // System.out.println(check);
        // System.out.println(check2);
        return check==check2?"Yes":"No";
        
        
    }
}