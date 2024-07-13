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

    email_split = email.split("@")
    email_test_one = 
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

    


















