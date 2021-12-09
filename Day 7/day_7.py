import statistics

with open("puzzle_input.txt") as file:
    data = file.read().rstrip()
    positions = list(map(int, data.split(",")))

# PART ONE
# Use median as middle point for all crabs to travel to
median = int(statistics.median(positions))
fuel_cost_1 = sum([abs(position - median) for position in positions])

# PART TWO
# Use mean as a middle point for all crabs to travel to
mean = int(statistics.mean(positions))
fuel_cost_2 = sum([sum(range(1, abs(position - mean) + 1)) for position in positions])

print(fuel_cost_1) # Part 1: 337488
print(fuel_cost_2) # Part 2: 89647695