start = input("Enter the range start: ")
end = input("Enter the range end: ")
start = int(start)
end = int(end)

colLength = len(oct(end))
print('{0:^{colLength}} {1:^{colLength}} {2:^{colLength}} {3:^{colLength}}'.format("Dec", "Hex", "Oct", "Bin", colLength=colLength))
for i in range(start, end + 1):
	print('{0:<{colLength}} {1:<{colLength}} {2:<{colLength}} {3:<{colLength}}'.format(i, hex(i).lstrip("0x"), oct(i).lstrip("0o"), bin(i).lstrip("0b"), colLength=colLength))
