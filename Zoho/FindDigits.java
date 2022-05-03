    // https://www.hackerrank.com/challenges/find-digits/problem
    
    public static int findDigits(int n) {
    // Write your code here
        int Number = n,currentNum,count=0;
        while (n!=0){
            currentNum = n%10;
            if(currentNum!=0 && Number % currentNum == 0){
                count++;
            } 
            n=n/10;
        }
        return count;
    }