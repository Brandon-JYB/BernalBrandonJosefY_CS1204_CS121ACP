import math
pi=math.pi
dim = int(input("Enter sphere diameter: "))
r=dim/2

SurAr = 4.00*pi*(r**2)

Vol = (4/3)*pi*(r**3)

print(f"Surface Area is {SurAr:.4f}")
print(f"Volume is {Vol:.4f}")