class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] != 9) {
                digits[i]++;
                return digits; // Return early if no carry is needed
            }
            digits[i] = 0; // Set to 0 if it's 9 and propagate the carry
        }

        // If we are here, all digits were 9, so we need a larger array
        int[] result = new int[digits.length + 1];
        result[0] = 1; // Set the leading 1
        return result;
    }
}
