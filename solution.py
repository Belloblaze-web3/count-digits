import sys

s = sys.stdin.readline().strip()
counts = [0] * 10

for ch in s:
    if ch.isdigit():
        counts[ord(ch) - ord('0')] += 1

for digit, count in enumerate(counts):
    print(digit, count)
