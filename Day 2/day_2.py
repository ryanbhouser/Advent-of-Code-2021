import csv

# PART ONE
with open("directions.csv") as file:
    data = csv.reader(file)
    h_dist = 0
    v_dist = 0
    # Loop through each row and add/subtract to the respective direction variable
    for row in data:
        if row[0] == "forward":
            h_dist += int(row[1])
        elif row[0] == "up":
            v_dist -= int(row[1])
        elif row[0] == "down":
            v_dist += int(row[1])
    # Answer to part 1 problem
    part_one_answer = h_dist * v_dist
    print(part_one_answer)
            
# PART TWO
with open("directions.csv") as file:
    data = csv.reader(file)
    h_dist = 0
    v_dist = 0
    aim = 0
    # Loop through each row and add/subtract to the respective direction variable
    for row in data:
        if row[0] == "forward":
            h_dist += int(row[1])
            v_dist += int(row[1]) * aim
        elif row[0] == "up":
            aim -= int(row[1])
        elif row[0] == "down":
            aim += int(row[1])
    # Answer to part 1 problem
    part_two_answer = h_dist * v_dist
    print(part_two_answer)