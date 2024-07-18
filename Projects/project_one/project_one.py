#initialize variables

email = ""
password=""
global successful_login
successful_login = False
global email_check 
global password_check
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
                    print("A valid password is alphanumeric and my contain special characters") #tells the password rules
                    password = input("Enter your password ") #gets user input for password
                    password_test = password.isascii() #checks for numbers, letters, special characters

                    if password_test == True: #if password contains valid input
                        print("The email and password are valid, login to finish account creation") #prints that the password is valid
                        password_check = True #sets password check to true

                        if email_check == True and password_check == True: #if email and password checks are ture
                            print("Enter your email") #asks for email
                            email_login = input() # gets input from user
                            if email == email_login: #if entered email is the same as saved email
                                print("Enter your password") #asks for password
                                password_login = input() #gets user input 
                                if password == password_login:
                                    print("Account successfully created, and you have been logged in") #prints confirmation message, and login message
                                    break #breaks while loop

                                else:#if password != the previous password
                                    print("Incorrect password, please try creating an account again")#print error message
                                    
                            else:#if email =! the previous email
                                print("Incorrect email, please try creating an account again")#print error message
                                
                        else:#if ascii check is false
                            print("Invalid password")#print error message
                            
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

    


















