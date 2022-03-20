// https://practice.geeksforgeeks.org/problems/leap-year0943/1/?page=3

class Solution{
    static int isLeap(int N){
        //code here
        boolean a = N%400==0 || N%4==0 && N%100!=0;
        return a==true?1:0;
    }
}