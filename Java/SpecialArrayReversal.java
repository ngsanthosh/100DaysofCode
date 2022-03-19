// https://practice.geeksforgeeks.org/problems/special-array-reversal2328/1#

class Solution
{
    public String reverse(String s)
    {
        //complete the function here
         //complete the function here
       char[] str=s.toCharArray();
       char a;
       for(int i=0,j=s.length()-1;i<s.length() && i<=j;)
       {
       if(!Character.isAlphabetic(str[i]))
       {
       i++;    
       }
       else if(!Character.isAlphabetic(str[j]))
       {
       j--;    
       }
       else
       {
       a=str[i];
       str[i]=str[j];
       str[j]=a;
       i++;
       j--;
       }
       }
//   String ans=String.valueOf(str);    
    return String.valueOf(str);
    }
}