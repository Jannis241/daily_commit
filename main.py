import os
import random
import uuid
from datetime import datetime

wanted_commits = None
variation = None

with open("info.txt", "r") as file:
    lines = file.readlines()

new_lines = []
for line in lines:
    if line.startswith("wanted_commits: "):
        wanted_commits = line.split(" ")[1].strip()
        print("Your current daily commits are:", wanted_commits)
        new_lines.append(line)
    elif line.startswith("range: "):
        variation = line.split(" ")[1].strip()
        print("The range is: ", variation)
        new_lines.append(line)
    else:
        new_lines.append(line)


if not wanted_commits:
    wanted_commits = input("How many commits do you want daily: ")
    new_lines.append("wanted_commits: " + wanted_commits + "\n")

if not range:
    variation = input("What should the range be: ")
    new_lines.append("range: " + str(range) + "\n")

with open("info.txt", "w") as file:
    file.writelines(new_lines)


now = datetime.now()
date = now.date()

date = date.strftime("%d.%m.%Y")


with open("log.txt", "r") as file:
    lines = file.read()


alreadyDoneToday = date in lines

print("Already done for today: ", alreadyDoneToday)
print()


def count_lines(filename):
    with open(filename, "r") as file:
        return sum(1 for _ in file)


def generateID():
    return str(uuid.uuid4())


def commitToGit(commits):

    if count_lines("change.txt") > 10000:
        with open("change.txt", "w"):
            pass

    for commit in range(commits):
        with open("change.txt", "a") as file:
            id = generateID
            file.write(f"New change from {date} | ID: {generateID()}\n")

        os.system("git add change.txt")
        os.system('git commit -m "daily commit"')
        os.system("git push origin main")

    input(f"Pushed {commits} times to git...")


if alreadyDoneToday:
    if input("Force it anyway (y/n): ") == "y":
        variation = int(variation)

        randomRangeNum = random.randint(-variation, variation)
        print("random num: ", randomRangeNum)
        commits = int(wanted_commits) + int(randomRangeNum)

        commitToGit(commits)
if not alreadyDoneToday:

    variation = int(variation)
    randomRangeNum = random.randint(-variation, variation)

    commits = int(wanted_commits) + int(randomRangeNum)

    with open("log.txt", "w") as file:
        file.write(date + "\n")

    commitToGit(commits)
