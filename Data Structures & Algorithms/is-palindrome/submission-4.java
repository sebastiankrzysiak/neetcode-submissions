class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) {
                l = l + 1;
            }
            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) {
                r = r - 1;
            }
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            l = l + 1;
            r = r - 1;
        }

        return true;
    }
}
