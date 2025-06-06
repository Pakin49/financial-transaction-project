#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(",")
    if columns[0] == "id":
        continue
    if len(columns) == 12:
        datetime = columns[1]
        date = datetime.split()[0]
        parts = date.split("-")
        year = parts[0]
        if year :
            try:
                print(f"{year}\t1")
            except ValueError:
                pass