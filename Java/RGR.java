// https://practice.geeksforgeeks.org/problems/red-or-green5711/1#

class Solution {
    static int RedOrGreen(int N, String S) {
        //code here
        int mini=Integer.MAX_VALUE;
        HashMap<Character, Integer> maps= new HashMap<Character, Integer>();
        
        for(int i=0;i<N;i++){
            if(maps.containsKey(S.charAt(i))){
                int old = maps.get(S.charAt(i));
                maps.put(S.charAt(i),old+1);
            }
            else{
                maps.put(S.charAt(i),1);
            }
        }
        // System.out.println(maps.toString());
        // return 0;
        // int arr=maps.keySet();
        for(int i: maps.values()){
            if(i<mini){
                mini=i;
            }
        }
        
       if(mini==N){
           return 0;
       }
       return mini;
    }
}