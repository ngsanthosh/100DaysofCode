import java.util.*;
public class Main
{
	public static void main(String[] args) {
		int number = 9;
		int[][] matrix = new int[number][number];
		int i=0,j=0;
		for(int iter=1;iter<=number*number;iter++){
		    if(iter==1){
		        i=number/2;
		        j=number-1;
		        matrix[i][j]=1;
		        
		    }
		    else{
		        if(i-1!=-1 && j+1!=number){
		            i=i-1;
		            j=j+1;
		            if(matrix[i][j]==0){
		                matrix[i][j]=iter;
		            }
		            else{
		                i=i+1;
		                j=j-2;
		                matrix[i][j]=iter;
		            }
		            continue;
		        }
		        else if(i-1==-1 && j+1!=number){
		            i=number-1;
		            j=j+1;
		            if(matrix[i][j]==0){
		              matrix[i][j]=iter;
		            }
		            else{
		                i=i+1;
		                j=j-2;
		                matrix[i][j]=iter;
		            }
		        }
		        else if(j+1==number && i-1!=-1){
		            i=i-1;
		            j=0;
		          if(matrix[i][j]==0){
		                matrix[i][j]=iter;
		            }
		            else{
		                i=i+1;
		                j=j-2;
		                matrix[i][j]=iter;
		            }
		        }
		        else if(i-1==-1 && j+1==number){
		            i=0;
		            j=number-2;
		            if(matrix[i][j]==0){
		                 matrix[i][j]=iter;
		            }
		            else{
		                i=i+1;
		                j=j-2;
		                matrix[i][j]=iter;
		            }
		        }
		    }
		}
		for(int row=0;row<matrix.length;row++){
		    for(int col=0;col<matrix[0].length;col++){
		        System.out.print(matrix[row][col]+" ");
		    }
		    System.out.println();
		}
	}
}
