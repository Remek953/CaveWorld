import os
import csv

def scores_load():
    if os.path.exists("Scores.csv") == True:
        with open("Scores.csv", "r") as file_object:
            reader =csv.DictReader(file_object)
            print(f"------------------------------------------------------------------------")
            print(f"| {'Name'.center(15, ' ')} | {'Race'.center(10, ' ')} | {'Class'.center(10, ' ')}"
                  f" | {'Kills'.center(10, ' ')} | {'Points'.center(10, ' ')} |")
            print(f"------------------------------------------------------------------------")
            for row in reader:
                print(f"| {row['Name'].center(15, ' ')} | {row['Race'].center(10, ' ')} | {row['Class'].center(10, ' ')}"
                      f" | {row['Kills'].center(10, ' ')} | {row['Points'].center(10, ' ')} |")
                print(f"------------------------------------------------------------------------")


    else:
        print("You have no scores in this game")









