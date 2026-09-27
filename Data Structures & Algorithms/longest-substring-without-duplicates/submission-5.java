class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int result = 0;
        int l = 0;
        int r = 0;

        while (r < s.length()) {
            if (!seen.contains(s.charAt(r))) {
                seen.add(s.charAt(r));
                r++;
                result = Math.max(result, r - l);
            }
            else {
                seen.remove(s.charAt(l));
                l++;
            }
        }
        return result;
    }
}
