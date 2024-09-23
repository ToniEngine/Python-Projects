# Slicing and Indexing in Python – Explained with Examples

'''
Indexing is the process of accessing an element in a sequence using 
its position in the sequence (its index).
In Python, indexing starts from 0, which means the first element in a 
sequence is at position 0, the second element is at position 1, and so on.
'''

my_list = ["apple", "banana", "cherry", "date"]
print(my_list)
print(my_list[0])  # Output: 'apple'
print(my_list[1])  # Output: 'banana'
print(my_list[2])  # Output: 'cherry'


'''
Slicing is the process of accessing a sub-sequence of a 
sequence by specifying a starting and ending index.
In Python, you perform slicing using the colon : operator. 
The syntax for slicing is as follows:
'''
# sequence[start_index:end_index]
print(my_list[1:3])   # Output: ['banana', 'cherry']


#You can also omit either the start_index or the end_index in a slice 
# to get all the elements from the beginning or end of the sequence. For example:
my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[:2]) # output: ['apple', 'banana']
print(my_list[2:]) # output: ['cherry', 'date']

sentence = "The quick brown fox jumps over the lazy dog"
first_word = sentence[0:3]
print(first_word)

second_word = sentence[4:9]
print(second_word)

third_word = sentence[10:15]
print(third_word)

# Suppose we have a list of numbers and we
# want to extract all the odd numbers from the list. We can do this using slicing as follows:
numbers =list("123456789")
print(numbers)
odd_numbers= numbers[0:9:2] #This can also be written as [::2]
print(odd_numbers)   # Output: ['1', '3', '5', '7', '9']

# We could also extract all the even numbers from the list using slicing as follows:
even_numbers =numbers[1::2]
print(even_numbers)    # Output: ['2', '4', '6', '8']



# How to Extract Columns from a 2D List
'''Suppose we have a 2D list representing a table of data,
 and we want to extract a particular column from the table. 
 We can do this using list comprehension and indexing as follows:'''


data = [[1,2,3], [4,5,6], [7,8,9]]
column = [row[1] for row in data]
print(column)

column_0 = [row[0] for row in data]
column_2 = [row[2] for row in data]
print(column_0) # output: [1, 4, 7]
print(column_2) # output: [3, 6, 9]