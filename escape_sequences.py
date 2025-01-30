num = int(input("How many multiples of 7?: "))

for i in range(1, num+1):
    if i%2==0:
        sum = 7*i
        print("\t", sum, end="\n")
    else:
        print((7*i),end="\n")