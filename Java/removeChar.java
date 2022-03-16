// https://practice.geeksforgeeks.org/problems/remove-character3815/0/#

class Solution{
    static String removeChars(String string1, String string2){
        // code here
        String out="";
        HashMap <Character,Integer> yes= new HashMap<>();
        for(int i=0;i<string2.length();i++){
            yes.put(string2.charAt(i),1);
        }
        
        for(int i=0;i<string1.length();i++){
            if(yes.containsKey(string1.charAt(i))){
                continue;
            }
            out+=string1.charAt(i);
        }
        return out;
    }
}