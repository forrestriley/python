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

    print("Emails should have valid valid username followed by an @, a mail server between 3 and 7 letters long, and end with a '.' before a three letter domain")

    #get input from user

    email = str(input("Please enter your email"))

    #check for valid email
    email = email.strip()#strips whitespace around input

    if email.find("@") > -1: #checks for  @ if found, execute
        email_split = email.split("@")#splits input at the @
        email_test_one = email_split[0].isalnum()#checks username for alphanumeric content and saves it to variable

        if email_test_one == True: #if test 1 is true execute
            email_test_two = email_split[1].find(".", -5,-3)


            if email_test_two == -4:
                email_test_three = email_split[1].find(".", -5,-3)

                if email_test_three == True:
                    email_check = True
                    print("A valid password is alphanumeric and my contain special characters")
                    password = input("Enter your password")
                    password_test = password.isascii()

                    if password_test == True:
                        print("The email and password are valid, login to finish account creation")
                        password_check = True

                        if email_check == True and password_check == True:
                            print("Enter your email")
                            email_login = input()
                            if email == email_login:
                                print("Enter your password")
                                password_login = input()
                                if password == password_login:
                                    print("Account successfully created, and you have been logged in")

                                else:#if test one is false execute
                                    print("Incorrect password, please try creating an account again")#print error message
                                    break#breaks loop
                            else:#if test one is false execute
                                print("Incorrect email, please try creating an account again")#print error message
                                break#breaks loop
                    else:#if test one is false execute
                        print("Invalid password")#print error message
                        break#breaks loop
                else:#if test one is false execute
                    print("No period detected before the three letter domain")#print error message
                    break#breaks loop
            else:#if test one is false execute
                print("No period detected before the three letter domain")#print error message
                break#breaks loop
        else:#if test one is false execute
            print("Invalid username for email")#print error message
            break#breaks loop
    else: #if no @ is found execute
        print("No @ found in the email, please try again.") #prints message for missing @
        break #breaks loop


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

    


















