slope = int(input("What do you want the slope to be?\n"))
a = 0
b = 0
c = 0
x = 0

while slope < 1 or slope > 11:
    print("Sorry, it needs to be between 1 and 10.")
    slope = int(input("What do you want the slope to be?\n"))

print(f"Your slope is {slope}")

time.sleep(2)

while a < 1 or a > 11:
    a = int(input("What do you want a to be?\n"))
while b < 1 or b > 11:
    b = int(input("What do you want b to be?\n"))
while c < 1 or c > 11:
    c = int(input("What do you want c to be?\n"))
while x < 1 or x > 11:
    x = int(input("What do you want x to be?\n"))
abc = (((a*x)^2) + (b*x) + c)
print(f"Your y is equal to: {abc}")
