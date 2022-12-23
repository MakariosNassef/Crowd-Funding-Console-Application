from registeration import *
from login import login
from sub_menu import sub_menu_fun


def register_menu():
    print("1- Sign in")
    print("2- Login")
    choice = (input("please enter your choice : "))
    print("*************************************")
    if choice.isdigit():
        if choice == '1':
            register_inputs()
        elif choice == '2':
            login()


        else:
            print("wrong choice")

    else:
        print("Must be a number")
        register_menu()


register_menu()
