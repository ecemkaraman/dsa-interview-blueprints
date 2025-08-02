## **🧠 Binary / Bitwise Strategy**
```python
Binary / Bitwise Problem
├── I. Bitwise Type (Bit Lens)
│   ├── bit manipulation (set / clear / toggle / check)
│   ├── bitmasking (subset representation)
│   ├── counting bits / parity
│   ├── shifts (<<, >>) for power-of-two logic
│   ├── XOR / AND / OR properties
│   └── low-level tricks (LSB, isolate rightmost set bit)

├── II. Input Type (Parse Layer)
│   ├── integer / array of ints
│   ├── binary string → convert to int if needed
│   ├── list of numbers → XOR / AND / OR aggregation
│   └── constraints hint binary → up to 32/64 bits

├── III. Algorithm Toolbox (Bitwise Engine)
│   ├── Basic Ops → & (mask), | (combine), ^ (toggle), ~ (invert)
│   ├── Shifts → << multiply by 2, >> divide by 2 (floor)
│   ├── Bit Counting → Brian Kernighan’s, DP, builtin popcount
│   ├── XOR Patterns → single number / missing number / subset xor
│   ├── Bitmask DP → subsets, TSP, assign workers, word problems
│   ├── Subset Generation → iterate 0..(1<<n), check bits
│   └── Tricks → x & (x-1) clears LSB, x & -x isolates LSB

└── IV. Pattern → Algorithm Mapping (Problem Intent)
    ├── Unique / Odd Occurrence
    │     ├── “find single / two unique nums in array”
    │     └── Use: XOR aggregation
    ├── Check / Toggle / Modify Bits
    │     ├── “is kth bit set / set kth bit / clear kth bit”
    │     └── Use: mask = 1<<k with & | ^
    ├── Count Bits / Parity
    │     ├── “count 1s / even parity / hamming weight”
    │     └── Use: n &= n-1 loop or builtin popcount
    ├── Subset / Power Set
    │     ├── “generate all subsets / mask states in DP”
    │     └── Use: iterate 0..(1<<n), check bits
    ├── Bitmask DP / State Compression
    │     ├── “TSP / assign workers / max compatibility”
    │     └── Use: dp[mask][state] transitions with bit ops
    └── Arithmetic / Optimization Tricks
          ├── “check power of 2 / swap without temp / divide fast”
          └── Use: n & (n-1), shifts, XOR swap

```