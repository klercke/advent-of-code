# d3p1.py
# Konnor Klercke
# Problem: Given a dataset of binary numbers, find the gamma and epislon rates
# such that the gamma rate contains the most common value for each binary
# place and the epsilon rate contains the least common value for each place


# This functions serves to read a list of binary numbers (as strs) and find
# the gamma and epsilon rates. This is probably super slow but it works
# Input:    List of same-size binary numbers stored as strings with \ns
# Output:   Gamma and Epsilon rates as strs in that order
def data2Rates(data):
    # Store these as strings so I can concat to them
    gamma = ''
    epsilon = ''

    # Determine the length of the binary values (disregarding \n)
    valueSize = len(data[0]) - 1

    # Loop over each binary place and determine the most common value
    for i in range(valueSize):
        # Reset the ones counter for each place
        ones = 0

        # Loop over each datapoint and record the number of ones
        for j in data:
            if j[i] == '1':
                ones += 1

        # Determine if there are more ones or zeroes in this place
        if ones > (len(data) - ones):
            gamma += '1'
            epsilon += '0'
        else:
            epsilon += '1'
            gamma += '0'

    # Return the rates as strings
    return gamma, epsilon


def main():
    # Open file, then close it once we're done reading the input
    with open('day3/d3.input', 'r') as file:
        # Make list of each line
        data = file.readlines()

    # Convert the data list into their rates, stored as binary numbers
    # represented by strings
    gamma, epsilon = data2Rates(data)

    # Print the numbers in binary, then their decimal equivalents, then the
    # product in decimal
    print("Gamma rate in Binary: " + gamma)
    print("Epsilon rate in binary: " + epsilon)
    print("Gamma rate in Decimal: " + str(int(gamma, 2)))
    print("Epsilon rate in Decimal: " + str(int(epsilon, 2)))
    print("Fuel consumption rate: " + str(int(gamma, 2) * int(epsilon, 2)))

if __name__ == "__main__":
    main()