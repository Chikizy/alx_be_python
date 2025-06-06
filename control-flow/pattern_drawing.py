size = int(input("Enter the size of the pattern:"))
num = size
while size > 0:
    for i in range(num):
        print("*", end="")
    print()
    size -= 1