import re
import time

class Organization:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.contact = ""
        self.mission = ""
        self.keyword = ""
        self.matched_list = {}

    def get_user_input(self, prompt):
        return input(prompt)

    def finish_registration(self):
        while True:
            name = self.get_user_input("Enter your name: ")
            email = self.get_user_input("Enter your email: ")
            contact = self.get_user_input("Enter your contact number: ")
            mission = self.get_user_input("Enter your organization's mission: ")
            keyword = self.get_user_input("Enter additional keywords: ")

            
            time.sleep(1)
            print("\n")

            goals = self.get_user_input("Almost done! What are you looking for? \n Select one or more from the following: \n Funding, Volunteers, Partnerships, Sponsorships, Mentors \n")
            goals_other = self.get_user_input("Optional: other goals?")
            description = self.get_user_input("And finaly, how would you describe your organization/company?")

            if not all([name, email, contact, mission, goals, description]):
                print("Error: Please fill in all the required fields.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("Error: Please enter a valid email address.")
            elif not re.match(r"^[0-9]{10}$", contact):
                print("Error: Please enter a valid 10-digit phone number.")
            else:
                completeness_percentage = 25 * 4
                print("Success: Registration complete! Completeness percentage: {}%".format(completeness_percentage))
                self.name = name
                self.email = email
                self.contact = contact
                self.mission = mission
                self.keyword = keyword
                self.all_goals = [goals, goals_other, description]
                self.show_personal_info(name, email, contact, mission, keyword)
                break

    def show_personal_info(self, name, email, contact, mission, keyword):
        personal_info = "Name: {}\nEmail: {}\nContact Number: {}\nMission: {}\nKeywords: {}".format(
            name, email, contact, mission, keyword
        )
        print("Personal Information:\n" + personal_info)
    
    # def get_org_data(self):
    #     return self.org_data


# from tkinter import *
# import tkinter.messagebox as tkMessageBox
# import re

# class ApplicationOrg(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         self.grid()
#         self.create_widgets()
#         org_data ={
#             "name": "",
#             "email": "",
#             "contact": "",
#             "mission": "",
#             "keyword": ""
#         }

#     def create_widgets(self):
#         self.name_label = Label(self, text="Name:")
#         self.name_label.grid(row=0, column=0, sticky=W)

#         self.email_label = Label(self, text="Email:")
#         self.email_label.grid(row=1, column=0, sticky=W)

#         self.contact_label = Label(self, text="Contact Number:")
#         self.contact_label.grid(row=2, column=0, sticky=W)

#         self.mission_label = Label(self, text="Organization Mission:")
#         self.mission_label.grid(row=3, column=0, sticky=W)

#         self.keyword_label = Label(self, text="Additional keywords:")
#         self.keyword_label.grid(row=4, column=0, sticky=W)

#         self.name_entry = Entry(self)
#         self.name_entry.grid(row=0, column=1)

#         self.email_entry = Entry(self)
#         self.email_entry.grid(row=1, column=1)

#         self.contact_entry = Entry(self)
#         self.contact_entry.grid(row=2, column=1)

#         self.mission_entry = Entry(self)
#         self.mission_entry.grid(row=3, column=1)

#         self.keyword_entry = Entry(self)
#         self.keyword_entry.grid(row=4, column=1)

#         self.finish_button = Button(self, text="Finish", command=self.finish_registration)
#         self.finish_button.grid(row=5, column=1)

#     def finish_registration(self):
#         name = self.name_entry.get()
#         email = self.email_entry.get()
#         contact = self.contact_entry.get()
#         mission = self.mission_entry.get()
#         keyword = self.keyword_entry.get()

#         if name == "" or email == "" or contact == "" or mission == "":
#             tkMessageBox.showerror("Error", "Please fill in all the required fields.")
#         elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             tkMessageBox.showerror("Error", "Please enter a valid email address.")
#         elif not re.match(r"^[0-9]{10}$", contact):
#             tkMessageBox.showerror("Error", "Please enter a valid 10-digit phone number.")
#         else:
#             completeness_percentage = 25 * 4
#             tkMessageBox.showinfo("Success", "Registration complete! Completeness percentage: {}%".format(completeness_percentage))
#             self.show_personal_info(name, email, contact, mission, keyword)

#             #update dictionary
#             self.org_data["name"] = name
#             self.org_data["email"] = email
#             self.org_data["contact"] = contact
#             self.org_data["mission"] = mission
#             self.org_data["keyword"] = keyword

#     def show_personal_info(self, name, email, contact, mission, keyword):
#         personal_info = "Name: {}\nEmail: {}\nContact Number: {}\nMission: {}\nKeywords: {}".format(name, email, contact, mission, keyword)
#         tkMessageBox.showinfo("Personal Information", personal_info)

    

