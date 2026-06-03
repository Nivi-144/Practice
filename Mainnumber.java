import java.util.Scanner;

public class Mainnumber {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        // input array
        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // hash array
        int[] hash = new int[13];

        // precompute frequency
        for(int i = 0; i < n; i++) {
            hash[arr[i]]++;
        }

        int q = sc.nextInt();

        while(q-- > 0) {

            int number = sc.nextInt();

            System.out.println(hash[number]);
        }

        sc.close();
    }
}
