# Challenge 3
# Created by: Zach Golik
# Date: 12/15/2014

import random


fathers = { "Dale": "Sam",
            "Darren":"Phillip",
            "Bowser": "Bowser Jr."}
randomGfather = ["Larry","Jacob","Link","Carson","Joel","Alex"]

choice = ""
while choice != "0":
    print(
        """
0 - Exit
1 - Add father son pair
2 - Remove father son pair
3 - Rename father son pair
4 - Find grandfather
"""
        )
    choice = input("Choice: ")

    
    if choice == "0":
        print("\nGoodbye.")

    
    if choice == "1":
       dad = input("\nEnter the fathers name: ")
       if dad not in fathers:
           son = input("\nEnter the name of the son: ")
           fathers[dad] = son
           print(fathers)
       else:
            print("\nThat dad is already listed.")

    
    if choice == "2":
        dad = input("\nWhat dad do you wan tme to delete? ")
        if dad in fathers:
            del fathers[dad]
            print(fathers)
        else:
            print("\nSorry that dad is not listed.")

    
    if choice == "3":
        dad = input("\nWhat dad's son name do you want to correct? ")
        if dad in fathers:
            son = input("\nWhat is the new name of the son? ")
            fathers[dad] = son
            print(fathers)
        else:
            print("\nSorry that dad is not listed.")
                 
    
    if choice == "4":
        father = input("\nEnter the name of the father: ")
        if father in fathers:
            if father == "Dale":
                 print("\nThe grandfather is Ryan.")
            elif father == "Darren":
                 print("\nThe grandfather name is Jordon.")
            elif father == "Bowser":
                 print("\nThe grandfahter is Bowser Senior.")
            else:
                 print("\nThe grandfather is",random.choice(randomGfather))
