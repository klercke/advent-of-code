# d2p1.py
# Konnor Klercke
# Problem: Given a submarine with possible commands of forward X, up X, and
# down X, read a list of these commands from an input file to determine the
# final position

# This functions serves to take a list containing up, down, and forward
# commands and return 2 lists containing only the integer deltas. Up is treated
# as a "negative down"
# Input:    List of commands, either forward X, up X, or down X
# Output:   List of horizontal values and list of vertical values
def separateData(data):
    dataHor = []
    dataVer = []
    for line in data:
        # Remove the newline character from each datapoint
        line = line.replace('\n', '')
        line = line.split(' ')

        # Deterimine which list the value should be in and add its integer
        # value to that list
        if (line[0] == 'forward'):
            dataHor.append(int(line[1]))
        elif (line[0] == 'down'):
            dataVer.append(int(line[1]))
        elif (line[0] == 'up'):
            # Going up is decreasing depth
            dataVer.append(-int(line[1]))
        else:
            # This doesn't happen in our dataset
            print("Error: Invalid command: " + data[0])

    return dataHor, dataVer


def main():
    # Open file, then close it once we're done reading the input
    with open('day2/d2.input', 'r') as file:
        # Make list of each line
        data = file.readlines()

    # Split our list of instructions into 2 lists of integers: one for depth,
    # and one for horizontal position
    dataHor, dataVer = separateData(data)

    # Add up the sums of each list
    totalHor = sum(dataHor)
    totalVer = sum(dataVer)

    # And finally print the sums and product for the prompt
    print("Total horizontal delta: " + str(totalHor))
    print("Total vertical delta: " + str(totalVer))
    print("Product: " + str(totalHor * totalVer))

if __name__ == "__main__":
    main()