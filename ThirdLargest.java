public class ThirdLargest {
    public static void main(String[] args) {
        int[] arr = {10, 25, 8, 45, 32, 18};

        int first = Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;
        int third = Integer.MIN_VALUE;

        for (int num : arr) {
            if (num > first) {
                third = second;
                second = first;
                first = num;
            } else if (num > second && num != first) {
                third = second;
                second = num;
            } else if (num > third && num != second && num != first) {
                third = num;
            }
        }

        if (third == Integer.MIN_VALUE) {
            System.out.println("Third largest element does not exist.");
        } else {
            System.out.println("Third Largest: " + third);
        }
    }
}
