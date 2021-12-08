with open("puzzle_input.txt") as file:
    data = file.read().rstrip()
    days = list(map(int, data.split(",")))

def count_lanternfish(limit):
    # Count how many fish have a specific number of days remaining before respawn
    days_remaining = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for day in days:
        days_remaining[day] += 1

    # While number of days is less than limit, find sum of fish after "limit" days
    count = 0
    while count < limit:
        temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # Shift previous day's number up to represent losing a day on the internal timer
        for i in range(len(days_remaining)):
            temp[i-1] = days_remaining[i]
        temp[6] += days_remaining[0] # When timer is 0, reset timer at 6
        temp[8] = days_remaining[0] # When timer is 0, spawn a new lanternfish
        days_remaining = temp
        count += 1
    return sum(days_remaining)

print(count_lanternfish(80)) # Part 1: 356131
print(count_lanternfish(256)) # Part 2: 1650309278600

# What I tried when the days = 80...then 256 happened... 
# while count < 80:
#         days[d] -= 1
#     for d in range(len(days)):
#         if days[d] == -1:
#             days[d] += 7
#             days.append(8)
#     count += 1

# print(len(days))
