# length check
# string check
# date check
# email validation
# postcode validation
# use calendar from tkinter

def email_validation(email):
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # using regex to check whether the email has the following characters

    if re.fullmatch(regex, email):
        return True
    else:
        return False


def length_check(text, length_required, choice):
    # choice is whether if the text should be equal to, greater than or less than
    if choice == 1:
        if len(text) == length_required:
            return True
        else:
            return False
    elif choice == 2:
        if len(text) >= length_required:
            return True
        else:
            return False

    else:
        if len(text) <= length_required:
            return True
        else:
            return False


def postcode_check(postcode):
    import requests

    response = requests.get("https://api.postcodes.io/postcodes/" + postcode)
    result = response.json()
    status = result.get("status")  # getting status code

    if status == 200:  # if status is 200 it means successful
        return True
    else:  # if status is not 200, it means there is no such postcode
        return False


def password_check(password):
    # must have uppercase, lowercase, numbers, characters and between 6 and 20 characters
    # importing re library
    import re
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    reg = re.compile(regex)
    # searching regex
    if re.search(reg, password):
        return True
    else:
        return False


if __name__ == "__main__":
    test1 = "veefaith15@gmail.com"
    print(email_validation(test1))

    test2 = "b34427@sfc.potteries.ac.uk"
    print(email_validation(test2))

    test3 = "ST3 5NP"
    print(postcode_check(test3))

    test4 = "Fight456#"
    print(password_check(test4))

    test5 = "ST3 5NP"
    print(postcode_check(test5))
