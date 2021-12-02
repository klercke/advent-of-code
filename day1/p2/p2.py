# day1/p1.py
# Konnor Klercke
# Problem: Given a dataset, determine how many sets of 3 concurrent datapoints
# have a larger sum that the set directly before it (such that they share two
# datapoints)


# This functions serves to convert the list of strings to a list of integers
# Input:    List of strings in the format '<int>\n'
# Output:   List of integers of the same size
def data2int(data):
    data_int = []
    for line in data:
        # Remove the newline character from each datapoint and convert it to
        # an int, then add it to a new list
        data_int.append(int(line.replace('\n', '')))
    return data_int


# This function will determine how many of the datapoints are a larger number
# (lower depth in the context of the problem) than the datapoint ahead of them
# Input:    List of integers
# Output:   Integer in range [0, len(data)-3)
def countIncreases(data):
    count = 0
    
    # Start counting at 1 since the first datapoint is N/A and stop on the
    # third-to-last datapoint since the frames are 3-points wide
    for i in range (1, len(data) - 2):
        # Set up the four datapoints we need to analyze...
        a = data[i - 1]
        b = data[i]
        c = data[i + 1]
        d = data[i + 2]

        # ...and determine the two sums...
        sum1 = a + b + c
        sum2 = b + c + d

        # ...and then see if the second sum is larger
        if (sum1 < sum2):
            count += 1

    return count


def main():
    # Open file, then close it once we're done reading the input
    with open('day1/p1/p1.input', 'r') as file:
        # Make list of each line
        data = file.readlines()

    # Convert the lines into integers
    data_int = data2int(data)
    
    # Count the number of depth increases
    increaseCount = countIncreases(data_int)

    # Print our output
    print("Total number of datapoints: " + str(len(data)))
    print("Total number of depth increases: " + str(increaseCount))
    
if __name__ == "__main__":
    main()