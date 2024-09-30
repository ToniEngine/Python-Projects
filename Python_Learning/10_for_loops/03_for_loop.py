prices = [10,20,30]
total = 0
for price in prices:
    total = total + price
print(f"Total: {total}")

### The code above and the code below does same thing
# But the one below is simple and lesser codes

total =sum([10,20,30])
print(f"Total: {total}")