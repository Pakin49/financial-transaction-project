#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    try:
        word, count = line.strip().split('\t')
        counts[word] += int(count)
    except Exception:
        # skip malformed lines
        continue

for word, count in counts.items():
    print(f"{word}\t{count}")
