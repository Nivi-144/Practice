import java.util.Scanner;

public class Solution {

    int fibonacci(int n) {

        // Base case
        if (n == 0 || n == 1) {
            return n;
        }

        // Recursive call
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter n:");
        int n = sc.nextInt();

        Solution obj = new Solution();

        int result = obj.fibonacci(n);

        System.out.println("Fibonacci number is: " + result);

        sc.close();
    }
}
