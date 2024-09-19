# ====================================
# A dictionary is a speacial structure in python that allows us to store information in key-value pairs
# You can access information in a dictionary by using it key
# This is synonymous to a dictionary in reality


# Building a program that converts a three digit month name to its full name
# Jan --> January
# The Keys have to be unique


monthConversions ={
    "Jan" : "January",
    "Feb":  "February",
    "Mar":   "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# print(monthConversions)

#==== Accessing the value by the Key
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv"))  # Output: None

#==== You can specify a default value using the get() function is the key is not found
#===  You can pass a default value that gets printed out

print(monthConversions.get("mun", "Not a valid key")) # Output: Not a valid key

