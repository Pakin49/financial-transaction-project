#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(",")
    if columns[0] == "id":
        continue
    if len(columns) == 12:
        merchant_state = columns[8]
        if merchant_state and merchant_state != "":
            try:
                print(f"{merchant_state}\t1")
            except ValueError:
                pass
