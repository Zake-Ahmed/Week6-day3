mark = float(input('Please input you mark '))

if mark>85:
    print("Distinction")
elif mark>65:
    print("Pass")
else:
    print("FAIL sorry :(")

if mark>85:
    print("Distinction")
if mark>65 and mark<85:
    print("Pass")
if mark<65:
    print("FAIL sorry :(")