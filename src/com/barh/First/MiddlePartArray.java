package com.barh.First;

public class MiddlePartArray {
    // Given an even numbered array, return the index at
    // which half of the array is is equal or less than the other

    static int isMiddlePartEqual(Integer[] arr) {
        int length = arr.length;
        int middle = length / 2 -1;
        int left_sum = 0;
        int right_sum = 0;
        for (int i = 0; i <= middle; i++) {
            left_sum += arr[i];
            right_sum+= arr[length-i-1];
        }
        left_sum -= arr[middle];
        while(middle >= 0 && left_sum >= right_sum){
            left_sum -= arr[middle--];
        }
        return middle+1;
    }

    public static void main(String[] args) {
        if (args.length == 0 || args.length%2 != 0){
            System.out.print("Not even parameters or empty array\n");
            System.exit(1);
        }
        Integer[] arr = new Integer[args.length];
        for(int i = 0; i < args.length; i++){
            arr[i] = Integer.valueOf(args[i]);
        }
        int ans = isMiddlePartEqual(arr);
        String s = String.valueOf(ans);
        if (ans == -1) s = "not exist";
        System.out.printf("Index is %s.\n", s);
        System.exit(0);
    }
}
