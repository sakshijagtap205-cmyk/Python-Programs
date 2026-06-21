import sys

num = float(input("Enter a value: "))

print("Value :", num)
print("Data Type :", type(num))
print("Memory Address :", hex(id(num)))
print("Size in Bytes :", sys.getsizeof(num))
