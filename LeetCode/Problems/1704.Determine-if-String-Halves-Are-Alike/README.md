# 1704. Determine if String Halves Are Alike

Time Complexity: O(n)
Space Complexity: O(1)

```python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel_set = set(['a', 'e', 'i', 'o', 'u'])
        half1_count, half2_count = 0, 0
        for i in range(len(s)):
            if i < len(s) // 2:
                if s[i].lower() in vowel_set:
                    half1_count += 1
            else:
                if s[i].lower() in vowel_set:
                    half2_count += 1
        return half1_count == half2_count
```