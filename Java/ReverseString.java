// https://practice.geeksforgeeks.org/problems/string-reversalunpublished-for-now5324/1#

class Solution
{
    public Boolean check(int x, String st){
        for(int i=0;i<st.length();i++){
            if(st.charAt(i)==x){
                return false;
            }
        }
        return true;
        
    }
    public String reverseString(String s)
    {
        String res="";
        for(int i=s.length()-1;i>=0;i--){
            if(s.charAt(i) ==' '){
                continue;
            }
            else{
                if(check(s.charAt(i),res)){
                    res+=s.charAt(i);
                }
            }
        }
        return res;
    }
}