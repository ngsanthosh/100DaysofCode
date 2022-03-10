// https://practice.geeksforgeeks.org/problems/non-repeating-character-1587115620/1#

class Solution
{
    // import java.util.HashMap;
    //Function to find the first non-repeating character in a string.
    static char nonrepeatingCharacter(String S)
    {
        //Your code here
        // S="apple";
        HashMap<Character,Integer> maps = new HashMap<Character,Integer>();
        
        for(int i=0; i<S.length();i++){
            if(maps.containsKey(S.charAt(i))){
                int old=maps.get(S.charAt(i));
                maps.put(S.charAt(i),old+1);
            }
            
            else{
                maps.put(S.charAt(i),1);
            }
            System.out.println(maps.toString());
        }
        
        for(int i=0; i<S.length();i++){
            if(maps.get(S.charAt(i))==1){
                return S.charAt(i);
            }
        }
        
        return '$';
        
    }
}