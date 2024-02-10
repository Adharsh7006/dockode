row = int(input("enter the row"))
cols = int(input("enter the column"))
value = int(cols / 2)
print("value",value)
data=int(cols-value)
print("data",data)

for i in range(0, row + 1):
    if i == 0:
        for j in range(0, data):
            print(" " * 1, "___", " " * 1, end=" ")
        print("\n", end=" ")
    if i != 0:
        for l in range(0, 1):
            for k in range(0, data):
                print("/", end=" ")
                print(" " * 1, "\\", end="")
                if k != data-1:
                    print("___", end="")
            print("\n", end=" ")
            for m in range(0, data):
                print("\\", end="")
                print("___", end="")
                print("/", " " * 1, end=" ")
            print("\n", end=" ")
