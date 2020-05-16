def duplicate(string):
	duplicateString=" "
for x in string:
	if x not in duplicateString :
		duplicateString = duplicateString +x
return duplicateString
S=input("Enter a string :")
print("After removing the duplicate character in the string, the new string is :",duplicate(S))