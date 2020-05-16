for i in range(8):
	for j in range(8):
			if j==i  or j==7-i :
				print("*", end="  ")
			else:
				print("  ",end="  ")
print()