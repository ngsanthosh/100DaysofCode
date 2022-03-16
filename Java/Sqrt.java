class Solution
{
     long floorSqrt(long x)
	 {
		// Your code here
		long i=1;
		long j=x;
		long ans=0;
		
		while(i<=j){
		    long mid=(i+j)/2;
		    if(mid*mid==x){
		        return mid;
		    }
		    else if(mid<=x/mid){ //or mid*mid <= x
		        i=mid+1;
		        ans=mid;
		    }
		    else{
		        j=mid-1;
		    }
		    
		}
		return ans;
	 }
}