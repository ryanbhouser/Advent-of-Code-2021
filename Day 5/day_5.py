# Parse file and create ordered pairs
with open("puzzle_input.txt") as file:
    lines = [line.strip().split(" -> ") for line in file.readlines()]
    pairs = [[coord.split(",") for coord in coord_pair]
             for coord_pair in lines]
    # Get list of all coordinates
    coordinates = [[list(map(int, i)) for i in pair] for pair in pairs]
    # Filter out all diagonal lines from coordinates
    hv_coordinates = [coord for coord in coordinates if coord[0]
                      [0] == coord[1][0] or coord[0][1] == coord[1][1]]

def get_overlaps(points):
    # Init a blank dictionary
    points_dict = {(x, y): 0 for x in range(1000) for y in range(1000)}
    for point in points:
        x1 = point[0][0]
        y1 = point[0][1]
        x2 = point[1][0]
        y2 = point[1][1]
        
        # Create horizontal points
        if x1 == x2:
            y_min, y_max = min(y1, y2), max(y1, y2)
            for y in range(y_min, y_max + 1):
                points_dict[(x1, y)] = points_dict.get((x1, y)) + 1

        # Create vertical points
        elif y1 == y2:
            x_min, x_max = min(x1, x2), max(x1, x2)
            for x in range(x_min, x_max + 1):
                points_dict[(x, y1)] = points_dict.get((x, y1)) + 1

        # Create diagonal points
        else:
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            for x in range(x1, x2 + 1):
                if y2 > y1:
                    y = y1 + (x - x1)
                else:
                    y = y1 - (x - x1)
                points_dict[(x, y)] = points_dict.get((x, y)) + 1

    return sum(overlap >= 2 for overlap in points_dict.values())

# Get number of overlaps
print(get_overlaps(hv_coordinates)) # Part 1: 5835
print(get_overlaps(coordinates)) # Part 2: 17013

