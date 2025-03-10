class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int pointerA = 0, pointerB = s.length() - 1;

        while (pointerA < pointerB) {
            if (s.charAt(pointerA++) != s.charAt(pointerB--)) return false;
        }
        
        return true;
    }
}