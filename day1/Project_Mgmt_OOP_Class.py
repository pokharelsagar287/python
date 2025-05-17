from datetime import datetime

#define a class to represent a project
class project:
    def __init__(self, name, deadline, budget, status="not started"):
        self.name = name
        self.deadline = deadline
        self.budget = budget
        self.status = status
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")

    # define a method to update the project status
    def update_status(self, new_status):
        self.status = new_status
        print(f"Project status updated to: {self.status}")

    # define a method to calculate the deadline
    def calculate_deadline(self):
        today = datetime.today()
        remaining_days = (self.deadline - today).days
        if remaining_days < 0:
            print("Project is overdue")
        elif remaining_days == 0:
            print("Project deadline is today")
        else:
            print(f"Project deadline is in {remaining_days} days")
            return remaining_days


    # define a method to print project details
    def print_project_details(self):
        print(f"Project Name: {self.name}")
        print(f"Project Deadline: {self.deadline.strftime('%Y-%m-%d')}")
        print(f"Project Budget: {self.budget}")
        print(f"Project Status: {self.status}")

#create an instance of the project class
project1 = project("Bridge construction", "2023-12-31", 1000000)

#show the project details
project1.print_project_details()

#update the project status
newstatus = input("Enter new project status: ")
project1.update_status(newstatus)

#show updated information
project1.print_project_details()

#save the project details to a file in tabular format
with open("project_details.txt", "w") as file:
    file.write(f"Project Name: {project1.name}\n")
    file.write(f"Project Deadline: {project1.deadline.strftime('%Y-%m-%d')}\n")
    file.write(f"Project Budget: {project1.budget}\n")
    file.write(f"Project Status: {project1.status}\n")
    file.write("\n")
    file.write("Project Details:\n")
    file.write("Name\tDeadline\tBudget\tStatus\n")
    file.write(f"{project1.name}\t{project1.deadline.strftime('%Y-%m-%d')}\t{project1.budget}\t{project1.status}\n")
    file.write("\n")
    file.write("Project Deadline Calculation:\n")