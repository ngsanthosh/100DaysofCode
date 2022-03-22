static void printPattern(String str, int len)
{
	for(int i = 0; i < len; i++)
	{
	for(int j = 0; j < len; j++)
	{

		// Print characters at corresponding
		// places satisfying the two conditions
		if((i == j) || (i + j == len - 1))
		System.out.print(str.charAt(j));

		// Print blank space at rest of places
		else
		System.out.print(" ");
	}

// 	System.out.println();
	}
}