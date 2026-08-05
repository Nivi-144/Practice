import java.util.*;
class anagrams{
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<>();
        if (s.length() < p.length())
            return ans;
        int[] pFreq = new int[26];
        int[] window = new int[26];
        for (char ch : p.toCharArray()) {
            pFreq[ch - 'a']++;
        }
        int k = p.length();
        for (int i = 0; i < s.length(); i++) {
            window[s.charAt(i) - 'a']++;
            if (i >= k) {
                window[s.charAt(i - k) - 'a']--;
            }
            if (Arrays.equals(window, pFreq)) {
                ans.add(i - k + 1);
            }
        }
        return ans;
    }
}
