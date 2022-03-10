class Solution{
    static int map(int n, String keys[], int arr[], String s)
    {
        // code here
        HashMap<String,Integer> maps = new HashMap<String,Integer>();
        
        for(int i=0;i<arr.length;i++){
            maps.put(keys[i],arr[i]);
        }
        
        if(maps.containsKey(s)){
            return maps.get(s);
        } 
        else{
            return -1;
        }
    }
}