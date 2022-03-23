import java.util.*;
public class HelloWorld{

     public static void main(String []args){
        int[] arr = {2,6,3,4,2,6,2,5,5,6,6,6};
        int n=arr.length;
        
        HashMap<Integer,Integer> map = new HashMap<>();
        
        for(int i=0;i<n;i++){
            if(map.containsKey(arr[i])){
                int old = map.get(arr[i]);
                map.put(arr[i],old+1);
            }
            else{
            map.put(arr[i],1);
            }
        }
        
        for(int j=0;j<n;j++){
            if(map.containsKey(arr[j])){
                System.out.println(arr[j]+"("+map.get(arr[j])+")");
                map.remove(arr[j]);
            }
        }
        
     }
}