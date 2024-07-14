#initialize variables

email = ""
password=""
successful_login = False
email_check = False
password_check = False
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
            email_test_two = email_split[1].find(".")

            if email_test_two == -4:
                email_test_three_variable = email_split[1].isalnum()
                email_test_three = 

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

    


















