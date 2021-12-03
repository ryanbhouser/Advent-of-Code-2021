# Generate list of binary numbers
with open("puzzle_input.txt") as file:
    lines = file.readlines()
    binary_numbers = [line.strip() for line in lines]

# Init the gamma and epsilon rates as strings
gamma_rate = ""
epsilon_rate = ""

# Loop through each column in binary_numbers to count number of 1s and 0s
for i in range(12):
    # Generate a list of each column
    numbers = [num[i] for num in binary_numbers]
    num_ones = 0
    num_zeroes = 0
    for j in numbers:
        if j == "1":
            num_ones += 1
        else:
            num_zeroes += 1
    # Append a 1 or 0 to the gamma and epsilon rates depending on which value appears more
    if num_ones > num_zeroes:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

# Convert the gamma and epsilon rates into decimal
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

# Get puzzle answer by multiplying both the gamma_rate and epsilon_rate
power_consumption = gamma_rate * epsilon_rate
print(power_consumption)  # 2583164
