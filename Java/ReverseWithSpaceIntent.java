class Solution
{
    String reverseWithSpacesIntact(String S)
    {
        // your code here
        String check="";
        
        int i=0;
        int j=S.length()-1;
        
        while(i<S.length() && j>=0){
            if(S.charAt(i) == ' '){
                check+=" ";
                i++;
            }
            else if(S.charAt(j) == ' '){
                j--;
                continue;
            }
            else{
                check+=S.charAt(j);
                i++;
                j--;
            }
        
        }
        return check;
    }
}