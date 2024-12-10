# imports date, time, csv, os python library
from datetime import datetime
import csv
import os


# makes sure daily_logs folder path exists
directory = "daily_logs"
os.makedirs(directory, exist_ok=True)


# opens and reads valid student/users id file
with open("users.txt", "r") as file:
    valid_user = {line.strip() for line in file}


# function for generation of daily logs within daily_logs folder path
def daily_log_generation(directory):
    current_date = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(directory, f"{current_date}.csv")

    #creates file if it doesnt exist # formats .csv file 
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Student ID","Status", "Date", "Time"])
    return file_path


# function verifying if student/user has signed in already
def student_already_signed_in(file_path, student_id):
    if not os.path.exists(file_path):
        return False
    with open(file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row["Student ID"] == student_id:
                return True
    return False


# function logging student sign in to csv file
def log_student_sign_in(file_path, student_id):
# variable assigned to store and generate time as string of text
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H-%M-%S")
    with open(file_path, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([student_id,"Signed In" ,current_date ,current_time])


# start of loop
while True:
# login variable assigned to users student id input
    login = input("STUDENT ID: ").strip()

#if statement validating the user login input is found in users.txt
    if login in valid_user:
        daily_log_file = daily_log_generation(directory)

        if student_already_signed_in(daily_log_file, login):
            print(f"{login} has already signed in today.")
        else:
            log_student_sign_in(daily_log_file, login)
            print ("Thank you, Welcome :)")
#else statement asking for user login input again 
    else:
        print("Please enter valid STUDENT ID");


