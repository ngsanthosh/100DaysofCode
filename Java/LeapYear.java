class Solution{
    static int isLeap(int N){
        //code here
        boolean a = N%400==0 || N%4==0 && N%100!=0;
        return a==true?1:0;
    }
}