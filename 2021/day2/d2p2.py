# d2p2.py
# Konnor Klercke
# Problem: Given a submarine with possible commands of forward X, up X, and
# down X, read a list of these commands from an input file to determine the
# final position

# This function takes the input data and determines final positions based on
# those commands
# Input:    List of commands, either forward X, up X, or down X
# Output:   Integers vertical and horizontal positions
def dataToPos(data):
    deltaX = 0
    deltaY = 0
    aim = 0
    for line in data:
        # Remove the newline character from each datapoint, split the command
        # from the value, and turn the value into an int
        line = line.replace('\n', '')
        line = line.split(' ')
        line[1] = int(line[1])

        # Determine what the command is telling us to do and adjust the deltas
        # as necessary
        if (line[0] == 'forward'):
            deltaX += line[1]
            deltaY += aim * line[1]
        elif (line[0] == 'down'):
            aim += line[1]
        elif (line[0] == 'up'):
            # Going up is decreasing depth
            aim -= line[1]
        else:
            # This doesn't happen in our dataset
            print("Error: Invalid command: " + data[0])

    return deltaX, deltaY


def main():
    # Open file, then close it once we're done reading the input
    with open('day2/d2.input', 'r') as file:
        # Make list of each line
        data = file.readlines()

    # Split our list of instructions into 2 lists of integers: one for depth,
    # and one for horizontal position
    deltaX, deltaY = dataToPos(data)

    # And finally print the sums and product for the prompt
    print("Total horizontal delta: " + str(deltaX))
    print("Total vertical delta: " + str(deltaY))
    print("Product: " + str(deltaX * deltaY))

if __name__ == "__main__":
    main()