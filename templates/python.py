# filename
# Konnor Klercke
# Problem:

# This functions serves to 
# Input:    
# Output:   
def foo(bar):
    return bar

def main():
    # Open file, then close it once we're done reading the input
    with open('input', 'r') as file:
        # Make list of each line
        data = file.readlines()

    print("Hello world!")

if __name__ == "__main__":
    main()