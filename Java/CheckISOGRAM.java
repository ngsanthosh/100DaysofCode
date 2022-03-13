class Solution
{
    //Function to check if a string is Isogram or not.
    static boolean isIsogram(String data){
        //Your code here
        HashMap<Character,Integer> hello = new HashMap<Character,Integer>();
        
        for(int i=0;i<data.length();i++){
            // System.out.println(hello.containsKey(data.charAt(i)));
            if(hello.containsKey(data.charAt(i))){
                return false;
            }
            hello.put(data.charAt(i),1);
        }
        return true;
    }
}