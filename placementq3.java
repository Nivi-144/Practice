import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int maximum = arr[0];
        int minimum = arr[0];

        for (int i = 1; i < n; i++) {

            if (arr[i] > maximum) {
                maximum = arr[i];
            }

            if (arr[i] < minimum) {
                minimum = arr[i];
            }
        }

        System.out.println("Maximum = " + maximum);
        System.out.println("Minimum = " + minimum);
    }
}
