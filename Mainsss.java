import java.util.Scanner;

public class Mainsss {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Input string
        String s = sc.next();

        // Hash array for characters
        int[] hash = new int[26];

        // Precompute frequency
        for(int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);

            hash[ch - 'a']++;
        }

        // Number of queries
        int q = sc.nextInt();

        while(q-- > 0) {

            char c = sc.next().charAt(0);

            System.out.println(hash[c - 'a']);
        }

        sc.close();
    }
}
