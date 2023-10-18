#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: October 18th, 2023
# this program asks the user for the month as a number between 1 to 12.


# this function will return the month in the string format.
def find_month(month):
    months = {
        1: "{} represents january.".format(month),
        2: "{} represents february.".format(month),
        3: "{} represents march.".format(month),
        4: "{} represents april.".format(month),
        5: "{} represents may.".format(month),
        6: "{} represents june.".format(month),
        7: "{} represents july.".format(month),
        8: "{} represents august.".format(month),
        9: "{} represents september.".format(month),
        10: "{} represents october.".format(month),
        11: "{} represents november.".format(month),
        12: "{} represents december.".format(month),
    }
    return (months.get(month, "Error. {} does not represent a month.".format(month)),)

# the user will input the month here
if __name__ == "__main__":
    user_month = int(input("Enter the number that represents the month: "))
    print(find_month(user_month))
