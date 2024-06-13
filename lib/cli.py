# lib/cli.py

# from helpers import (
#     exit_program,
#     helper_1
# )

#import sys
from models.lawyer import Lawyer
from models.client import Client
from models.cases import Case

def main_menu():
    while True:
        print("Main Menu")
        print("1. Manage Lawyers")
        print("2. Manage Clients")
        print("3. Manage Cases")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_lawyers()
        elif choice == "2":
            manage_clients()
        elif choice == "3":
            manage_cases()
        elif choice == "4":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

def manage_lawyers():
    while True:
        print("Manage Lawyers")
        print("1. Add Lawyer")
        print("2. Delete Lawyer")
        print("3. View All Lawyers")
        print("4. Find Lawyer by ID")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter lawyer's name: ")
            specialty = input("Enter lawyer's specialty: ")
            lawyer_id = Lawyer.create_lawyer(name, specialty)
            print(f"Lawyer created with ID: {lawyer_id}")
        elif choice == "2":
            lawyer_id = input("Enter lawyer ID to delete: ")
            Lawyer.delete_lawyer(lawyer_id)
            print(f"Lawyer with ID {lawyer_id} deleted.")
        elif choice == "3":
            lawyers = Lawyer.get_all_lawyers()
            for lawyer in lawyers:
                print(lawyer)
        elif choice == "4":
            lawyer_id = input("Enter lawyer ID to find: ")
            lawyer = Lawyer.view_by_id(lawyer_id)
            print(lawyer)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_clients():
    while True:
        print("Manage Clients")
        print("1. Add Client")
        print("2. Delete Client")
        print("3. View All Clients")
        print("4. Find Client by ID")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter client's name: ")
            contact_info = input("Enter client's contact information: ")
            lawyer_id = input("Enter lawyer ID: ")
            client_id = Client.create_client(name, contact_info, lawyer_id)
            print(f"Client created with ID: {client_id}")
        elif choice == "2":
            client_id = input("Enter client ID to delete: ")
            Client.delete_client(client_id)
            print(f"Client with ID {client_id} deleted.")
        elif choice == "3":
            clients = Client.get_all_clients()
            for client in clients:
                print(client)
        elif choice == "4":
            client_id = input("Enter client ID to find: ")
            client = Client.find_client_by_id(client_id)
            print(client)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
def manage_cases():
    while True:
        print("Manage Cases")
        print("1. Add Case")
        print("2. Delete Case")
        print("3. View All Cases")
        print("4. Find Case by ID")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter case title: ")
            description = input("Enter case description: ")
            lawyer_id = input("Enter lawyer ID: ")
            case_id = Case.create_case(title, description, lawyer_id)
            print(f"Case created with ID: {case_id}")
        elif choice == "2":
            case_id = input("Enter case ID to delete: ")
            Case.delete_case(case_id)
            print(f"Case with ID {case_id} deleted.")
        elif choice == "3":
            cases = Case.get_all_cases()
            for case in cases:
                print(case)
        elif choice == "4":
            case_id = input("Enter case ID to find: ")
            case = Case.find_case_by_id(case_id)
            print(case)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
