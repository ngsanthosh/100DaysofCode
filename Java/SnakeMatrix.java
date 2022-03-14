// https://practice.geeksforgeeks.org/problems/print-matrix-in-snake-pattern-1587115621/1#

class Solution
{
    //Function to return list of integers visited in snake pattern in matrix.
    static ArrayList<Integer> snakePattern(int matrix[][])
    {
        // code here 
        int row=matrix.length;
        int col=matrix[0].length;
        ArrayList<Integer> vec = new ArrayList<Integer>();
        
        for(int i=0;i<row;i++){
            if(i%2==0){
                for(int j=0;j<col;j++){
                    vec.add(matrix[i][j]);
                }
            }
            else{
                for(int j=col-1;j>=0;j--){
                    vec.add(matrix[i][j]);
                }
            }
            
        }
        return vec;
    }
}