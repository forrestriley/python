#imports
import re #imports regex

#initialize variables

email = ""
password=""
global successful_login
successful_login = False
global email_check 
email_check = False
global password_check
password_check = False
# while loop checking for a successful login

while successful_login == False:

    # print prompt stating email requirements tom@

    print("Emails should have valid valid username followed by an @, a mail server between 3 and 7 letters long, and end with a '.' before a 3 to 5 letter domain")

    #get input from user

    email = str(input("Please enter your email "))

    #check for valid email
    email = email.strip()#strips whitespace around input



    if email.find("@") > -1: #checks for  @ if found, execute
        email_split = email.split("@")#splits input at the @
        email_test_one = email_split[0].isalnum()#checks username for alphanumeric content and saves it to variable
         

        if email_test_one == True: #if test 1 is true execute
            email_test_two = email_split[1].find(".", -5,-2) #checks for a "." between the fifth and third to last characters in 

            if email_test_two != -1: #if find is able to locate a '.' in the correct area
                    email_check = True #sets email check to true
                    if password_check == False:
                        print("A valid password is must be at least 8 characters long with no spaces, contain at least one uppercase letter, one lowercase letter, one number, and at least one of the following: !, ?, @, #, $, ^, &, _, -") #tells the password rules
                        password = input("Enter your password ") #gets user input for password
                        length = len(password) #sets length to pass length
                        if length >= 8: #checks for password length being 8 or more
                            
                            pass_test_one = password.find(" ")#checks for whitespace, returns -1 if none were detected

                            if pass_test_one == -1:
                                        
                                        if not re.search("[a-z]", password): #checks for at least one lower case letter
                                            print("No lower case letters found") # if fails print designated error
                                        elif not re.search("[A-Z]", password): #checks for at least one capitol letter
                                            print("No upper case letters found") # if fails print designated error
                                        elif not re.search("[0-9]", password): #checks for at least one digit
                                            print("No number detected", password) # if fails print designated error
                                        elif not re.search("[!?@#$^&*_-]", password): #checks for at least one of the specified characters
                                            print("Must include at least one !, ?, @, #, $, ^, &, _, or -") # if fails print designated error
                                        else:
                                            password_check = True
                                            print("Password Accepted")

                                            if email_check == True and password_check == True: #if email true
                                                print("Enter your email") #asks for email
                                                email_login = input() # gets input from user
                                                if email == email_login: #if entered email is the same as saved email
                                                    print("Enter your password") #asks for password
                                                    password_login = input() #gets user input 
                                                    if password == password_login:
                                                        print("Account successfully created, and you have been logged in") #prints confirmation message, and login message
                                                        break #breaks while loop

                                                    else:
                                                        print("Incorrect Password, please try creating an account again")#prints failure message
                                                else:#if email =! the previous email
                                                    print("Incorrect email, please try creating an account again")#print error message
                            else:
                                print("Invalid password, spaces were detected")
                        else: #if the password is too short
                            print(f"The password was not long enough, it was only {length} characters long") #prints out error, and length of entered password                                       
            else:#if '.' is not detected in range
                print("No period detected before the domain")#print error message
        else:#if there is no valid input before @
            print("Invalid username for email")#print error message
    else: #if no @ is found execute
        print("No @ found in the email, please try again.") #prints message for missing @
        


    #print prompt stating password requirements

    #get input from user

    #check for valid password

    #if email and password are valid

        #prompt to login using selected email 

        #if email input is valid

            #if password is valid

                #successful login, successful_login = True
            
            # else login failure, loop break

        #else login failure, loop break

    


















