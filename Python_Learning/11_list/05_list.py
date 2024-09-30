# A program that iterates over a list of number and prints the highest number in the list


numbers = [3,6,2,100,1000, 8,4,10]
max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)