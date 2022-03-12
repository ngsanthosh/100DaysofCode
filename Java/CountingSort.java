// #ERROR 
// Counting sort: GFG

class Solution
{
    //Function to arrange all letters of a string in lexicographical 
    //order using Counting Sort.
    public static String countSort(String arr)
    {
        // code here
        Integer[] arrr = new Integer[26];
        
        // return "";
        for (int i=0;i<26;i++){
            arrr[i]=0;
        }
        // System.out.println(Arrays.toString(arrr));
        // return "";
        
        for(int i=0;i<arr.length();i++){
            int temp = (int) arr.charAt(i)-97;
            arrr[temp]++;
        }
        String res="";
        for (int i=0;i<26;i++){
            for (int j=0;j<arrr[i];j++){
                res+=(char)(i+97);
            }
        }
        
        return res;
        
        
    }
}