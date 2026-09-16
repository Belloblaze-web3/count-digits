# Count Digits

Given a string `S`, count how many times each digit from `0` through `9` occurs.

## Approach

Maintain an array of ten counters. For every character in the input string, increment the counter corresponding to that digit, then print all ten counters in order.

## Complexity

- Time: `O(|S|)`
- Space: `O(1)`

## Run

```bash
python3 count_digits.py
```

### Sample input

```text
77150
```

### Sample output

```text
0 1
1 1
2 0
3 0
4 0
5 1
6 0
7 2
8 0
9 0
```
