import re
import json

user_id = 0


def register_inputs():
    global user_id
    user_id = user_id + 1
    first_name = input("Enter your First name :")
    first(first_name)
    last_name = input("Enter your Last name :")
    last(last_name)
    email = check_mail()
    password = input("Enter your password :")
    conf_password = input("confirm your password :")
    phone = input("plz Enter your Phone : ")
    print("***************************************")
    check_password(password, conf_password)
    phone_check(phone)
    data = fill_data(user_id, first_name, last_name, email, password, conf_password, phone)
    data_list = read_file()
    data_list.append(data)
    write_data(data_list)


def read_file():
    with open("data_file.json", "r") as read_file:
        data_returned = json.load(read_file)
        return data_returned


def write_data(data_list):
    with open("data_file.json", "w") as write_file:
        json.dump(data_list, write_file)


def fill_data(user_id, first_name, last_name, email, password, conf_password, phone):
    data = {
        "user_id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "confirm_password": conf_password,
        "phone": phone
    }
    return data


def phone_check(phone):
    res = re.match("(01)[0-9]{9}", phone)
    if not res:
        print("Enter valid phone Number")


def check_string(text):
    if re.match("^[0-9]*$", text):
        return 0
    elif text == "":
        return 1


def first(first_name):
    val1 = check_string(first_name)
    if val1 == 0:
        print("Must be String Not a Number")
    elif val1 == 1:
        print("Must not be empty")
        first_name = input("Reenter your First_name  again:")


def last(last_name):
    val1 = check_string(last_name)
    if val1 == 0:
        print("Must be String Not a Number")
        last_name = input("Reenter your Last_name  :")
    elif val1 == 1:
        print("Must not be empty")
        last_name = input("Reenter your Last_name  :")


def check_register_status():
    print("Register Y/N")
    register = input("")
    if register == 'y' or 'Y':
        print("successfully registerd")
    else:
        print("you undo register")


def check_mail():
    email = input("Enter your Email :")
    if not re.match('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email):
        email = input("ReEnter your Email  again:")
    return email


def check_password(password, conf_password):
    if password != conf_password:
        print("password and confirmation don't match ")
