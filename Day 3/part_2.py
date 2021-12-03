# Generate list of binary numbers
with open("puzzle_input.txt") as file:
    lines = file.readlines()
    binary_numbers = [line.strip() for line in lines]

# Takes in a list and the o2 or co2 type and counts number of 1s and 0s in each column
def get_life_support_rating(data, type):
    for i in range(12):
        num_ones = 0
        num_zeroes = 0
        for j in data:
            if j[i] == "1":
                num_ones += 1
            else:
                num_zeroes += 1
        # Filters values from data based on whether a 1 or 0 appears in the list
        if num_ones >= num_zeroes:
            data = list(filter(lambda x: x[i] == (
                "1" if type == "oxygen" else "0"), data))
        else:
            data = list(filter(lambda x: x[i] == (
                "0" if type == "oxygen" else "1"), data))
        if len(data) == 1:
            break
    # Returns the value as an integer converted to decimal
    return int(data[0], 2)

# Calls a function called get_life_support_rating to get value or o2 and co2
oxygen_generator_rating = get_life_support_rating(binary_numbers, "oxygen")
co2_scrubber_rating = get_life_support_rating(binary_numbers, "c02")

# Final answer by multiplying oxygen_generator_rating and co2_scrubber_rating
life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(life_support_rating) # 2784375
