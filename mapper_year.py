#!/usr/bin/env python3
import sys

def clean_amount(snum):
    negative = False
    res = ""
    for char in snum:
        if char == "$":
            continue
        if char == "-":
            negative = True
            continue
        res += char
    clean_num = float(res)
    if negative:
        clean_num *= -1 
    return clean_num

for line in sys.stdin:
    line = line.strip()
    columns = line.split(",")
    if columns[0] == "id":
        continue
    if len(columns) == 12:
        datetime = columns[1]
        amount = clean_amount(columns[4])
        date = datetime.split()[0]
        parts = date.split("-")
        year = parts[0]
        if year :
            try:
                print(f"{year}\t1\t{amount}")
            except ValueError:
                pass