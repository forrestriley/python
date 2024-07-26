# define list of numbers
list_of_numbers = [2,6,8,34,66,155]

#  define function
def mean_of_list(list): # takes in data as 'list'
    return (sum(list) / len(list)) # returns the sum of list divided by the length of the list

# print statement 
print("Mean of list:", round(mean_of_list(list_of_numbers), 2)) # calls the mean of list function, taking in list of numbers as 'list' and the returned value is rounded to two decimal points, and printed after the str