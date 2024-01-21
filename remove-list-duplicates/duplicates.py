r = int(input("range: "))

rlist = []

# before remove duplicates
for x in range(r):
    new_x = int(input("x: "))
    rlist.append(new_x)

print(rlist)

# after remove duplicate
rlist = list(dict.fromkeys(rlist))

print(rlist)
