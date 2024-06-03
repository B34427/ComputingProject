from tkinter import *
# changes the default/old password to a new one
# takes in the password as a parameter
def get_username():
    form = Tk()
    form.title("Change Password")
    form.geometry("500x200")
    # creating the username label, old password and new password labels

    usernameLabel= Label(form, text="Username")
    usernameLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")
    oldpassLabel = Label(form, text="Old Password")
    oldpassLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")
    newpassLabel = Label(form, text="New Password")
    newpassLabel.grid(row=3, column=0, padx=10, pady=10, sticky="W")
    # creating the username, old password and new password entry
    usernameEntry = Entry(form, width=20)
    usernameEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")
    oldpassEntry = Entry(form, width=20, show="*")
    oldpassEntry.grid(row=2, column=1, padx=10, pady=10, sticky="E")
    newpassEntry = Entry(form, show="*")
    newpassEntry.grid(row=3, column=1, padx=10, pady=10, sticky="W")
    # create the exit and submit buttons
    exitButton = Button(form, text="Exit", width=12, command=quit)
    exitButton.grid(row=4, column=1, padx=10, pady=10, sticky="W")
    submitButton = Button(form, text="Submit", width=12)
    submitButton.grid(row=4, column=0, padx=10, pady=10, sticky="W")
    # set the focus to the username box
    usernameEntry.focus()
    form.eval('tk::PlaceWindow . center')
    mainloop()

get_username()
