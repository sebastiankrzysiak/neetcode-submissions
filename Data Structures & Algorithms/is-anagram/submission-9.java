class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sMap = new HashMap<>();
        HashMap<Character, Integer> tMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            sMap.put(s.charAt(i), sMap.getOrDefault(s.charAt(i), 0) + 1);
        }

        for (int j = 0; j < t.length(); j++) {
            tMap.put(t.charAt(j), tMap.getOrDefault(t.charAt(j), 0) + 1);
        }

        return sMap.equals(tMap);
    }
}
