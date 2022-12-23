import re
import json

project_id = 0


def project_details(user_id):
    title = input("Enter your project title: ")
    details = input("Enter your project details: ")
    total_target = int(input("Enter your target : "))
    start_date = input('Enter start date in YYYY-MM-DD format: ')
    check_date(start_date)
    end_date = input("Enter end date in YYYY-MM-DD format: ")
    check_date(end_date)
    append_data(user_id, title, details, total_target, start_date, end_date)


def check_date(date):
    if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}", date):
        print("accepted")
    else:
        print("Enter valid date")


def append_data(user_id, title, details, total_target, start_date, end_date):
    global project_id
    data_list = get_data()
    project_id = project_id + 1
    project_data = {
        "user_id": user_id,
        "project_id": project_id,
        "project_title": title,
        "project_details": details,
        "total_target": total_target,
        "start_date": start_date,
        "end_date": end_date

    }
    data_list.append(project_data)
    write_data(data_list)


def write_data(data_list):
    with open("project_database.json", "w") as write_file:
        json.dump(data_list, write_file)


def get_data():
    with open("project_database.json", "r") as read_file:
        data_returned = json.load(read_file)

    return data_returned


def view_all_projects():
    data_list = get_data()
    for project in data_list:
        print(project)


def edit_project(user_id):
    data_list = get_data()
    project_id = int(input("Enter the project id you want to edit:"))

    for project in data_list:
        if project["user_id"] == user_id:
            if project["project_id"] == project_id:
                print(project)
                updated_project = project
                new_user_project_title = input("Enter your new  project tiltle  :")
                if not new_user_project_title:
                    new_user_project_title = project["project_title"]
                else:
                    updated_project["project_title"] = new_user_project_title
                new_user_project_details = input("Enter your new project details: ")
                if not new_user_project_details:
                    new_user_project_details = project["project_details"]
                else:
                    updated_project["project_details"] = new_user_project_details
                new_total_target = input("Enter your new Total Target :")
                if not new_total_target:
                    new_total_target = project["total_target"]
                else:
                    updated_project["total_target"] = new_total_target
                new_start_date = input("Enter your new start date: ")
                if not new_start_date:
                    new_start_date = project["start_date"]
                else:
                    updated_project["start_date"] = new_start_date
                new_end_date = input("Enter your new end date:")
                if not new_end_date:
                    new_end_date = project["end_date"]
                else:
                    updated_project["end_date"] = new_end_date
                project = updated_project
                write_data(data_list)
                break

    else:
        print("Not Found This Project ID")


def delete_project(user_id):
    data_list = get_data()
    project_id = int(input("Enter th project id you want to delete:"))

    for project in data_list:
        if project["user_id"] == user_id:
            if project["project_id"] == project_id:
                print(project)
                data_list.remove(project)
                write_data(data_list)
                view_all_projects()
                break


def search_project(user_id):
    data_list = get_data()
    project_date = input("Enter th project start date:")
    check_date(project_date)
    for project in data_list:
        if project["user_id"] == user_id:
            if project["start_date"] == project_date:
                print(project)
