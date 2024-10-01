# string ="abcd"
# for s in range(len(string)):
#     print(s[::-1], end="")

# string = "abcd"
# for s in range(len(string)):
#     print(string[::-1], end="")


string = "abcd"
for s in range(len(string) - 1, -1, -1):
    print(s, end="")

