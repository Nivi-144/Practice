import java.util.*;

class HuffmanCoding {
    static class Node {
        char ch;
        int freq;
        Node left, right;

        Node(char ch, int freq) {
            this.ch = ch;
            this.freq = freq;
        }

        Node(int freq, Node left, Node right) {
            this.freq = freq;
            this.left = left;
            this.right = right;
        }
    }

    static void generateCodes(Node root, String code) {
        if (root == null)
            return;
        if (root.left == null && root.right == null) {
            System.out.println(root.ch + " : " + code);
            return;
        }

        generateCodes(root.left, code + "0");
        generateCodes(root.right, code + "1");
    }

    public static void main(String[] args) {

        char[] chars = {'a', 'b', 'c', 'd', 'e', 'f'};
        int[] freq = {5, 9, 12, 13, 16, 45};

        // Min Heap based on frequency
        PriorityQueue<Node> pq =
            new PriorityQueue<>((a, b) -> a.freq - b.freq);

        for (int i = 0; i < chars.length; i++) {
            pq.add(new Node(chars[i], freq[i]));
        }

        while (pq.size() > 1) {

            Node left = pq.poll();
            Node right = pq.poll();

            Node parent = new Node(
                left.freq + right.freq,
                left,
                right
            );

            pq.add(parent);
        }

        Node root = pq.poll();
        System.out.println("Huffman Codes:");
        generateCodes(root, "");
    }
}
