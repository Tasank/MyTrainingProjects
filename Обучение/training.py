table = [[''] * 10 for i in range(1, 11)]
print()
print('    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |')
for i, row in enumerate(table):
    row_str = f"  {i} | {' | '.join(row)}"
    print(row_str)
    print('  -------------------------------------------')