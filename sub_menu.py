from project import *
import os

def sub_menu_fun(user_id):
    os.system("clear")
    print('\n =============[ MENU ]===============')
    print(" 1- Add new Project")
    print(" 2- View All Projects")
    print(" 3- Edit Project")
    print(" 4- Delete Project")
    print(" 5- Search by Date")
    choice = input("\n    Enter your Selection: ")
    if choice.isdigit():

        if choice == '1':
            project_details(user_id)
        elif choice == '2':
            view_all_projects()
        elif choice == '3':
            edit_project(user_id)
        elif choice == '4':
            delete_project(user_id)
        elif choice == '5':
            search_project(user_id)
        else:
            print("Wrong choice")
    else:
        print('\n  Please select from the Menu.')
    sub_menu_fun(user_id)
