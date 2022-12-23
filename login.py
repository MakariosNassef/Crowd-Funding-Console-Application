import json
from registeration import read_file, check_mail
from sub_menu import sub_menu_fun

user_id = ""


def login():
    login_email = check_mail()
    login_password = input("Enter your password : ")
    deserialize_data(login_email, login_password)


def deserialize_data(login_email, login_password):
    global user_id

    data = read_file()
    for user in data:
        if user['email'] == login_email and user['password'] == login_password:
            print("successfully login")
            print("*************************************")
            user_id = user['user_id']
            sub_menu_fun(user_id)

            break
    else:
        print("Wrong login")
