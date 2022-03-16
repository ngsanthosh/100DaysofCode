class Solution
{
    public int maxChars(String s)
    {
        //code here
        HashMap<Character,Integer> map = new HashMap<>();
        int largest=-1;
        
        for(int i=0;i<s.length();i++){
            if(map.containsKey(s.charAt(i))){
                largest=Math.max(largest,i - map.get(s.charAt(i)) - 1);
            }
            else{
            map.put(s.charAt(i),i);
            }
        }
        return largest;
    }
}