/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
// palindrome program without using extra space and without splitting the array
public class Main
{
	public static void main(String[] args) {
		String a="RACECAR";
		int i=0;
		int j=a.length()-1;
// 		int flag=0;
		while (i<a.length()-1 && j>=0){
		    if(a.charAt(i)==a.charAt(j)){
		        
		        i++;
		        j--;
		        continue;
		}
		else{
		    System.out.println("Not a Palindrome");
		    return;
		}
		}
		System.out.println("Palindrome");
		
// 		while (j>=0){
		    
// 		}
		
// 		for(int i=0;i<a.length();i++){
// 		    for(int j=a.length()-1;j>=0;j--){
// 		        System.out.println(a.charAt(i));
// 		        System.out.println(a.charAt(j));
// 		        if(a.charAt(i)==a.charAt(j)){
		            
// 		            continue;
// 		        }
// 		        else{
// 		            System.out.println("Not a palindrome");
// 		            break;
// 		        }
		        
// 		    }
// 		}
		
	}
}
