# great alternatives to lists
# fast, easy to work with, calcuation across entire arrays

import numpy as np

# example case
bb = [66.5, 75.2, 60.5, 67.9, 77.4, 70.2, 51.5, 65.5]
tb = [1.43, 1.64, 1.31, 1.58, 1.78, 1.54, 1.56, 1.75]

np_bb = np.array(bb)
np_tb = np.array(tb)

# check the data type
print(type(np_bb))
print(type(np_tb))

# calculate bmi
bmi = np_bb / (np_tb **  2)

print(bmi)

for i in range(len(bmi)):

    if bmi[i] < 18.5:
        print("----- Kurang BB ----")
    elif bmi[i] > 18.5 and bmi[i] <= 24.9:
        print("--- Normal ---- ")
    elif bmi[i] > 25 and bmi[i] <= 29.9:
        print("---- overweight ----")
    elif bmi[i] > 30:
        print(f"---- obesitas ----")

    print(f"BMI[{i}] = {bmi[i]}")