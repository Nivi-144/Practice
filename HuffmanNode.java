import java.util.PriorityQueue;

class HuffmanNode {
    int freq;
    char ch;
    HuffmanNode left, right;

    HuffmanNode(char ch, int freq) {
        this.ch = ch;
        this.freq = freq;
    }
}

public class HuffmanCoding {

    static void printCodes(HuffmanNode root, String code) {
        if (root == null)
            return;

        if (root.left == null && root.right == null) {
            System.out.println(root.ch + " : " + code);
            return;
        }

        printCodes(root.left, code + "0");
        printCodes(root.right, code + "1");
    }

    public static void main(String[] args) {

        char[] chars = {'A', 'B', 'C', 'D', 'E', 'F'};
        int[] freq = {5, 9, 12, 13, 16, 45};

        PriorityQueue<HuffmanNode> pq =
                new PriorityQueue<>((a, b) -> a.freq - b.freq);

        for (int i = 0; i < chars.length; i++) {
            pq.add(new HuffmanNode(chars[i], freq[i]));
        }

        while (pq.size() > 1) {
            HuffmanNode left = pq.poll();
            HuffmanNode right = pq.poll();

            HuffmanNode parent = new HuffmanNode('-', left.freq + right.freq);
            parent.left = left;
            parent.right = right;

            pq.add(parent);
        }

        HuffmanNode root = pq.poll();

        System.out.println("Huffman Codes:");
        printCodes(root, "");
    }
}
