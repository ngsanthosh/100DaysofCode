class GfG
{
    boolean callme(int j,String ss,String find){
        int z=0;
        while(j<ss.length() && z<find.length()){
            if(ss.charAt(j)==find.charAt(z)){
                j++;
                z++;
            }
            else{
                return false;
            }
        }
        if(z==find.length()){
            return true;
        }
        else{
            return false;
        }
    }
    //Function to locate the occurrence of the string x in the string s.
    int strstr(String s, String x)
    {
       // Your code here
       for(int i=0;i<s.length();i++){
           if(s.charAt(i)==x.charAt(0)){
               if(callme(i,s,x)){
                //   if(i==s.length()-1){
                //       return -1;
                //   }
                   return i;
               } 
           }
       }
       return -1;
    }
}