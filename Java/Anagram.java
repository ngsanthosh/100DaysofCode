class Solution
{    
    //Function is to check whether two strings are anagram of each other or not.
    public static boolean isAnagram(String a,String b)
    {
        
        // Your code here
        HashMap<Character,Integer> map = new HashMap<>();
        
        for(int i=0;i<a.length();i++){
            if(map.containsKey(a.charAt(i))){
                int old = map.get(a.charAt(i));
                map.put(a.charAt(i),old+1);
            }
            else{
            map.put(a.charAt(i),1);
            }
        }
        // System.out.println(map);
        for(int i=0;i<b.length();i++){
            if(map.containsKey(b.charAt(i)) && map.get(b.charAt(i))>=1){
                int oldd = map.get(b.charAt(i));
                map.put(b.charAt(i),oldd-1);
            }
            else{
                // System.out.println(i);
                return false;
            }
        }
        return true;
        
        
    }
}