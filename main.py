#!/usr/bin/env python3

# Created by : Mr. Coxall
# Created on : October 2019
# This program prints out your name, using default function parameters


def full_name(first_name,last_name, middle_name = None):
    # return the full NameError

    full_name = first_name
    if middle_name != None:
        full_name = full_name + " " + middle_name[0]
    full_name = full_name + " " + last_name

    return full_name
    
def main():
    # gets a users name and prints out their formal name
    middle_name = None
    
    first_name = input("Enter your first name: ")
    question = input("Do you have a middle name? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")

    if middle_name != None:
        name = full_name(first_name, last_name, middle_name)
    else:
        name = full_name(first_name, last_name)

    print(name)

if __name__ == "__main__":
    main()
