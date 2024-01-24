input_range = int(input("Enter range: "))

nlist = []

# start from index 0
for n in range(input_range):
    n = int(input("Enter number: "))
    nlist.append(n)

print(f"Your List number        : {nlist}")
# nlist.reverse()
# print(f"Your Reverse List number: {nlist}")
# or
print(f"Your Reverse List number: {nlist[::-1]}")







