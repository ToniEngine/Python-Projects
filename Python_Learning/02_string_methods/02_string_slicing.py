# slicing can be used to create a substring by extracting elements from another string
#       indexing[] or slice()
#       [start:stop:step]
#       with slicing there are 3 optional arguments with regards to where we want to slice our string

name = "Anthony Obot"
first_name = name[0:7]  # [:7]
print(first_name)

last_name = name[8:] 
print(last_name)

# step is how much we are increasing our index by starting and stoping
# Normally step is one by default
# If we set step to 2 , it counts only every second character

funky_name = name[0:12:1]
print(funky_name)

funky_name = name[0:12:2]  # [::2]
print(funky_name)


# How to reverse a string in python
reversed_name = name[::-1]
print(reversed_name)



# ========== Using the slice() function ============
# We can use the slice() function to create a slice object that is reusable
website = "http://google.com"
slice =slice(7, -4)

print(website[slice]) 



website2 = "http://wikipedia.com"
print(website2[slice])


website3 = "https://tenergystores.com"
print(website3[8:-4])

