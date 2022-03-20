class Solution {
    // Function to return the count of the number of elements in
    // the intersection of two arrays.
    public static int NumberofElementsInIntersection(int a[], int b[], int n, int m) {
        // Your code here
        HashMap<Integer,Integer> map = new HashMap<>();
        // HashMap<Integer,Integer> map1 = new HashMap<>();
        for(int i=0;i<m;i++){
            map.put(b[i],0);
        }
        int count=0;
        for(int i=0;i<n;i++){
            if(map.containsKey(a[i])){
                count++;
                map.remove(a[i]);
            }
        }
        return count;
    }
};