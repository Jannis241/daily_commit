import os
from datetime import datetime

username = None
wanted_commits = None

with open("info.txt", "r") as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    if line.startswith("username: "):
        username = line.split(" ")[1].strip()
        print("Your username is:", username)
        if input("Do you want to change your username (y/n): ") == "y":
            username = input("What is your username: ")
            new_lines.append("username: " + username + "\n")
        else:
            new_lines.append(line)
    elif line.startswith("wanted_commits: "):
        wanted_commits = line.split(" ")[1].strip()
        print("Your current daily commits are:", wanted_commits)
        if input("Do you want to change your daily commits (y/n): ") == "y":
            wanted_commits = input("How many commits do you want daily: ")
            new_lines.append("wanted_commits: " + wanted_commits + "\n")
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

if not username:
    username = input("What is your username: ")
    new_lines.append("username: " + username + "\n")

if not wanted_commits:
    wanted_commits = input("How many commits do you want daily: ")
    new_lines.append("wanted_commits: " + wanted_commits + "\n")

with open("info.txt", "w") as file:
    file.writelines(new_lines)

with open("info.txt", "r") as file:
    print(file.read())


now = datetime.now()
date = now.date()

date = date.strftime("%d.%m.%Y")


with open("log.txt", "r") as file:
    lines = file.read()


alreadyDoneToday = date in lines

print("Already done for today: ", alreadyDoneToday)
print()


def commitToGit():

    for commit in range(int(wanted_commits)):
        with open("change.txt", "a") as file:
            lines = len(file.readlines())
            file.write(f"Change for the {date}: {commit}\n")

        os.system("git add .")
        os.system('git commit -m "daily commit"')
        os.system("git push origin main")


if alreadyDoneToday:
    if input("Force it anyway (y/n): ") == "y":
        commitToGit()

if not alreadyDoneToday:

    with open("log.txt", "w") as file:
        file.write(date + "\n")

    commitToGit()
