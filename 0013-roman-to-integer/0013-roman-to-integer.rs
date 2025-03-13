use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let roman: HashMap<char, i32> = [
            ('I', 1), ('V', 5), ('X', 10),
            ('L', 50), ('C', 100), ('D', 500),
            ('M', 1000)
        ].iter().cloned().collect();

        let mut sum = 0;
        let mut prevValue = *roman.get(&s.chars().nth(0).unwrap()).unwrap();
        
        for c in s.chars().skip(1) {
            let currentValue = *roman.get(&c).unwrap();
            if currentValue > prevValue {
                sum -= prevValue;
            } else {
                sum += prevValue;
            }
            prevValue = currentValue;
        }
        sum + prevValue
    }
}