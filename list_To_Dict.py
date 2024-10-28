##### Create a List in a range from 1 to 10 #####
# Create a list containing numbers from 1 to 9 (inclusive) using the range function.
list_10 = list(range(1, 10))
print(list_10)  

##### Create a List multiplying the first list x2 #####
# Create a new list by multiplying each element in the original list by 2 using a list comprehension.
list_10_x2 = [i * 2 for i in list_10]
print(list_10_x2)  

#### Transform ####
# Combine the two lists into a list of tuples using the zip function. 
# Each tuple contains elements from the original list and the multiplied list at the same index.
list_result = zip(list_10, list_10_x2)
print(list_result) 

#### Convert the zip object into a dictionary, where the first list's elements become the keys ####
# and the second list's elements become the values.
dictionarie_list = dict(list_result)
print(dictionarie_list) 