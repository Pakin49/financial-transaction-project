#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(lambda: [0, 0.0])
for line in sys.stdin:
    try:
        word, count, tol_amount = line.strip().split('\t')
        counts[word][0] += int(count)
        counts[word][1] += float(tol_amount)
    except Exception:
        continue

for word,(count,total) in counts.items():
    average = total/count
    print(f"{word}\t{count}\t{total}\t{average}")
