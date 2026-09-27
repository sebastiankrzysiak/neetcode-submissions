class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> parenToParen = new HashMap<>();
        
        parenToParen.put('(', ')');
        parenToParen.put('{', '}');
        parenToParen.put('[', ']');

        ArrayList<Character> stack = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            if (parenToParen.containsKey(s.charAt(i))) {
                stack.add(s.charAt(i));
            }
            else {
                if (stack.isEmpty()) {
                    return false;
                }
                else {
                    char leftParen = stack.removeLast();
                    if (parenToParen.get(leftParen) != s.charAt(i)) {
                        return false;
                    }
                }
            }
        }
        if (stack.isEmpty()) {
            return true;
        }
        return false;
    }
}
