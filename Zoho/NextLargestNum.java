import java.util.*;
public class Main
{
	public static void main(String[] args) {
		int[] a = {3,54,62,2,12,59};
        ArrayList<Integer> res = new ArrayList<>();
        int n = a.length;
        int temp;
        for(int i=0;i<n;i++){
          temp = -1; 
          for(int j=i+1;j<n;j++){
            if(temp==-1){
                if(a[j]>a[i]){
                  temp=a[j];
                }
            }
            else{
                if(a[j]<temp && a[j]>a[i]){
                  temp=a[j];
                }
            }
          }
          res.add(temp);
        }
        System.out.println(res);

	}
}