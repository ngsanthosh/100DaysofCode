public class Main
{
	public static void main(String[] args) {
		int n=5;
        for(int i=1;i<=n;i++){
            for (int j=i;j<=n;j++){
                System.out.print(j+" ");
            }
            for (int z=1;z<i;z++){
                System.out.print(z+" ");
            }
            System.out.println();
        }
	}
}

// 1 2 3 4 5
// 2 3 4 5 1
// .......