# imports time date and time python library
from datetime import datetime

# opens and reads students id text file
with open("users.txt", "r") as file:
    valid_user = {line.strip() for line in file}

# variable assigned to store and generate time as string of text
current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# start of loop
while True:
# login variable assigned to users student id input
    login = (input("STUDENT ID: "))

#if statement validating the user login input is found in users.txt
    if login in valid_user:
        print ("Thank you, Welcome :)")
#else statement asking for user login input again 
    else:
        print("Please enter valid STUDENT ID");
#log.txt is opened and logs login attempts with date and time
    log = open("log.txt", "a")
    log.write(f"{login} logged in at {current_time}\n")
