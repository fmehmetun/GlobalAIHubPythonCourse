## 1 - Create a list and swap halves of it, then print it out.

# Create list
myList = [42,43,44,45,46, 47,48,49,50,51]

# Get half index
halfPoint = len(myList)//2

# Slice first and second half of the list
firstHalf = myList[:halfPoint]
secondHalf = myList[halfPoint:]

# Concatenate halves to create final swapped list
mySwappedList = (secondHalf + firstHalf)

print("Original list: ", myList)
print("Halves swapped: ", mySwappedList)

## 2 - Get single digit from user. Then through 0 to n print out even numbers.

# Get input and check if single digit given
n = int(input("Enter a single digit integer: "))
if (len(str(n)) == 1):
	# n+1 for including n
	for i in range(0, n+1):
		# Check if even
		if i%2 == 0:
			print(i)
else:
	print("This is not a single digit integer.")
