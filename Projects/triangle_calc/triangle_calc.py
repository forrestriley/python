'''
Triangle Calculator
'''

'''
Write a program that will calculate the area of a triangle, below is the equation needed to solve this problem

Area of Triangle= 1/2 x base x height
For your example, base = 20, height = 15
Requirements
-Comment your code
-use proper naming for your variables
-Include a string within your print built in function that says, "The area of your triangle is " as output (formatted string)
'''

# initiates base as user's input
base = input("Enter Triangle's Base Length   ")

while ( base.isdigit() != True ):# checks if the input was a valid number, if False it runs the loop
  base = input("Enter Triangle's Base Length   ")# re-assigns the value of base to the new user input
  if base.isdigit() == True:# if they entered a number it breaks the loop, otherwise the loop continues to ask for valid input
    break

# initiates height as user's input
height = input("Enter Triangle's Height   ")

while ( height.isdigit() != True):# checks if the input was a valid character, if False it runs the loop
  height = input("Enter Triangle's Height   ")# re-assigns the value of height to the new user input
  if height.isdigit() == True:# if they entered a character it breaks the loop, otherwise the loop continues to ask for valid input
    break

# sets the variable to 1/2 x base x height | base and height are made integers from strings via built in function
area_of_triangle = (1/2 * int(base) * int(height))

#  Prints the text with formated string to put the variable directly into the str
print(f"The area of your triangle is {area_of_triangle}.")








