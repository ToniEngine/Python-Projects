# Nested Loops = adding one loop inside another loop
# We can use this to generate a list of coordinates
# (x,y)


for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

# == exrecise ==
numbers =[5,2,5,2,2]
for x_count in numbers:
    print("x" * x_count)
    
print("")
print("")
# Using an inner loop
numbers_1 =[2,2,2,5,5]
for x_count in numbers_1:
    output= ""
    for count in range(x_count):
        output += "x"
    print(output)