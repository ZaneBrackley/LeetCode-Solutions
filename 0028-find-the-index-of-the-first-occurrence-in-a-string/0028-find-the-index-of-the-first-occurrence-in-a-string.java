class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() > haystack.length()) return -1;
        for (int i = 0; i < haystack.length() - needle.length() + 1; i++) {
            if (haystack.charAt(i) == needle.charAt(0)) {
                String subHaystack = haystack.substring(i, i + needle.length());
                if (subHaystack.equals(needle)) {
                    return i;
                }
            }
        }
        return -1;
    }
}