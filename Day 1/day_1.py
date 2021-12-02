# Get depths from depths.txt
with open("depths.txt", "r") as file:
    lines = file.readlines()
    # Add each line into a list named "depths"
    depths = [int(line.rstrip()) for line in lines]
    # Add sum of every sequential trio to a list named "trios"
    depth_trios = [sum([depths[i], depths[i+1], depths[i+2]])
                   for i in range(len(depths)-2) for depth in depths]

# Compares the first value of a list with the next
def compare_depths(list):
    count = 0
    first = list[0]
    for i in list:
        if i > first:
            count += 1
        first = i
    return count


# Call compare_depths for "depths" and "trios" lists
print(compare_depths(depths))  # 1624
print(compare_depths(depth_trios))  # 1653
