class Solution
{
    ArrayList<Long> findMissing(long A[], long B[], int N, int M)
    {
        HashMap<Long,Integer> map = new HashMap<Long,Integer>();
        ArrayList<Long> res = new ArrayList<Long>();
        for(int i=0;i<M;i++){
            // if(map.containsKey(B[i])){
                
            // }
            map.put(B[i],1);
        }
        for(int i=0;i<N;i++){
            if(map.containsKey(A[i])){
                continue;
            }
            res.add(A[i]);
        }
        return res;
    }
}