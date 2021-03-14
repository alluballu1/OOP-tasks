# File name: exercise8task3.py
# Author: Alex Porri
# Description: Creating a list of 10 cookies with selected flavoring and frosting.

from CookieClass import Cookie

# Creating the baking function

def bake_cookies(list_of_cookies):
    flavor = input("What kind of cookies do you want to make?: ")
    for each in range(10):
        cookie = Cookie(flavor)
        list_of_cookies.append(cookie)
    return list_of_cookies

# Creating the frosting function

def frosting_cookies(list_of_cookies):
    frosting_flavor = input("What kind of frosting would you like?: ")
    for each in list_of_cookies:
        each.set_frosting(frosting_flavor)
    return list_of_cookies

# Creating the main function

def main():
    list_of_cookies = []
    start = input("Bake cookies, Y/N?: ")
    if start == "N":
        print("Okay.")
        exit()
    if start == "Y":
        bake_cookies(list_of_cookies)
        frosting_cookies(list_of_cookies)
    checkup = input("Is " + list_of_cookies[0].get_flavor() + " flavored cookies with " + list_of_cookies[0].get_frosting()
                    + " frosting your favorite type of cookies, Y/N?: ")
    if checkup == "Y":
        print("Enjoy the batch of " + str(len(list_of_cookies)) + " cookies!")
    else:
        print("Starting again.")
        main()

main()



