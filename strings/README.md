## **🧠 String Strategy**

```python
String Problem
├── I. String Type (String Lens)
│   ├── (in)case-sensitive
│   ├── small (a–z) / large charset (Unicode)
│   ├── single / pair / list[str]
│   ├── static / stream
│   └── plain / pattern-present / palindrome-leaning

├── II. Input Type (Parse Layer)
│   ├── raw string s
│   ├── two strings (s, t) → compare / mapping / anagram
│   ├── list[str] → group / frequency / tries
│   ├── text + pattern → substring search
│   └── dictionary/wordlist → word break / trie

├── III. Algorithm Toolbox (String Engine)
│   ├── Two Pointers → compare, reverse, trim, expand-around-center
│   ├── Sliding Window + Counter → longest/min substr with constraints
│   ├── Hashing → rolling hash (Rabin–Karp), substring hashes
│   ├── KMP / Z → linear-time pattern matching
│   ├── Trie / Prefix Map → prefixes, autocomplete, word-break speedup
│   ├── DP → edit distance, LCS, decode ways, regex-like matching
│   ├── Stack → parentheses, decode string, remove duplicates
│   ├── Counting / Sorting → anagrams (26-count / sort key)
│   └── Manacher (adv) → longest palindromic substring O(n)

└── IV. Pattern → Algorithm Mapping (Problem Intent)
    ├── Substring with property
    │     ├── “longest no-repeat / ≤K distinct / min window”
    │     └── Sliding Window + Counter/need map
    ├── Anagram(s)
    │     ├── “are anagrams? / find all anagrams”
    │     └── 26-count (a–z) or hashmap (+ window for “find all”)
    ├── Palindrome
    │     ├── “check / longest pal substring”
    │     └── Two Pointers / Expand-around-center (Manacher adv)
    ├── Parentheses / Canonicalization
    │     ├── “valid / min remove / decode 3[a2[c]]”
    │     └── Stack (+ count/greedy for min remove)
    ├── Pattern Search
    │     ├── “find pattern in text / first occurrence”
    │     └── KMP / Z (Rabin–Karp ok for simplicity)
    ├── Edit / Transform
    │     ├── “edit distance / one edit away / LCS”
    │     └── DP (Levenshtein / LCS), two pointers for “one edit”
    ├── Word Break / Segmentation
    │     ├── “segment s using dict / all sentences”
    │     └── DP + set (Trie/DFS for all sentences, memo)
    ├── Frequency / Top-K
    │     ├── “top-k words / most common”
    │     └── HashMap + Heap / Bucket sort
    ├── Isomorphic / Bijection
    │     ├── “same pattern mapping?”
    │     └── Two hash maps (s→t, t→s)
    └── Parsing / Version / Cleanup
          ├── “compare versions / normalize / strip”
          └── Two Pointers / split+parse / state machine
```