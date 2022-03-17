// https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?isFullScreen=false

class Result {

    public static void plusMinus(List<Integer> arr) {
    // Write your code here
    Double pos=0.0;
    Double neg=0.0;
    Double zero=0.0;
    
    for(int i=0;i<arr.size();i++){
        if(arr.get(i)>0){
            pos++;
        }
        else if(arr.get(i)<0){
            neg++;
        }
        else{
            zero++;
        }
    }
    double posra = pos/arr.size();
    double negra = neg/arr.size();
    double zerora = zero/arr.size();
    
    System.out.printf("%.6f",posra);
    System.out.printf("\n%.6f",negra);
    System.out.printf("\n%.6f",zerora);
    }

}