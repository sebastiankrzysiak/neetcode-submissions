class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> charToCount = new HashMap<>();
        int result = 0;
        int l = 0;
        int r = 0;

        while (r < s.length()) {
            charToCount.put(s.charAt(r), charToCount.getOrDefault(s.charAt(r), 0) + 1);
            while (r - l + 1 - Collections.max(charToCount.values()) > k) {
                charToCount.put(s.charAt(l), charToCount.get(s.charAt(l)) - 1);
                l++;
            }
            result = Math.max(result, r - l + 1);
            r++;
        }

        return result;
    }
}
