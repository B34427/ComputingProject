from tkinter import *
from project_validation import *

# login window which will open once run.
def login_window():
    form = Tk()
    # form title
    form.title("Welcome")
    form.geometry("500x200")
    # the subtitle label on the top of the screen
    subtitleLabel = Label(form, text="Please log in to your account")
    subtitleLabel.config(font=("San Fransico", 14), justify="center")
    subtitleLabel.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)
    # creating the username and password labels
    usernameLabel = Label(form, text="Username:")
    usernameLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    passwordLabel = Label(form, text="Password:")
    passwordLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")
    # creating the username entry box
    usernameEntry = Entry(form)
    usernameEntry.grid(row=1, column=1, padx=10, pady=10, sticky="W")
    # creating the password entry box
    passwordEntry= Entry(form)
    passwordEntry.grid(row=2, column=1, padx=10, pady=10, sticky="W")

    alternativeLabel = Label(form, text="Forgot password")
    alternativeLabel.grid(row=1, rowspan=2, column=2, padx=10, pady=10)
    # creating text-boxes (entry boxes):
    userEntry = Entry(form, width="30")
    userEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")
    passEntry = Entry(form, width="30", show='*')  # Show * to hide the password
    passEntry.grid(row=2, column=1, padx=10, pady=10, sticky="E")
    # creating the buttons:
    exitButton = Button(form, text="Exit", width=12, command=quit)
    exitButton.grid(row=3, column=0, padx=10, pady=10)

    #enterButton = Button(form, text="Clear", width=12, command=lambda: clearboxes(form, userEntry, passEntry))
    #enterButton.grid(row=3, column=1, padx=10, pady=10)

    #enterButton = Button(form, text="Enter", width=12, command=lambda: get_login(form, userEntry, passEntry))
    # later we add command to call a function
    #enterButton.grid(row=3, column=2, padx=10, pady=10)

    userEntry.focus()  # set the focus to eightEntry box (the top one)
    # makes it easy to user to avoid clicking the box before
    # we enter the data
    form.eval('tk::PlaceWindow . center')

    mainloop()

login_window()