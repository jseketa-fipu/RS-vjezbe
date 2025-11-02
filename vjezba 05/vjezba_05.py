# only "loops" once, prints out 1
for i in range(1, 2):
    print(i)

# first breakpoint
# doesn't loop at all, start index greater then stop index
for i in range(10, 1, 2):
    print(i)

# second breakpoint
# counts back from 10 to 1 (1 not included, beware !=)
for i in range(10, 1, -1):
    print(i)
