import os
import time
import csv


# Load scoreboard from Scores.csv
def scores_load():

    """
    Load scores from Scores.csv and sort the points from highest to lowest.
    """

    time.sleep(0.5)
    os.system("cls")

    if os.path.exists("Scores.csv") == True:
        with open("Scores.csv", "r") as file_object:
            reader = csv.DictReader(file_object)
            sort_scores = sorted(reader, key=lambda row: int(row["Points"]), reverse=True)

            print(f"------------------------------------------------------------------------")
            print(f"| {'Name'.center(15, ' ')} | {'Race'.center(10, ' ')} | {'Class'.center(10, ' ')}"
                  f" | {'Kills'.center(10, ' ')} | {'Points'.center(10, ' ')} |")
            print(f"------------------------------------------------------------------------")

            for row in sort_scores:
                print(f"| {row['Name'].center(15, ' ')} | {row['Race'].center(10, ' ')} | {row['Class'].center(10, ' ')}"
                      f" | {row['Kills'].center(10, ' ')} | {row['Points'].center(10, ' ')} |")
                print(f"------------------------------------------------------------------------")

    else:
        print("You have no scores in this game")