import java.util.*;
public class Main
{
	public static void main(String[] args) {
		int[] a={1,2,3,4,5};
		int[] b={6,7,8,9,10};
		
		int[] c={0,0,0,0,0}; 
        // int[] c = new int[a.length]; -- Alternate if size is to be fixed
		for(int i=0;i<a.length;i++){
		    c[i]=a[i]+b[i];
		}
		
		System.out.println(Arrays.toString(c));
	}
}