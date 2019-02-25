import string

def print_rangoli(size):
    width = size * 4 - 3
    L = []

    # Create list of letters up to size
    pattern = string.ascii_letters[:size]

    # Create half of the output lines
    for i in range(size):
        # Create half of each line separating each letter with a '-'.
        # Creates lines with most letters first (center to outer)
        temp = '-'.join(pattern[i:size])

        # Concat the reversal of the line created with the oringal form
        # Center the string with a length of 'width' and filling with '-'
        L.append((temp[::-1] + temp[1:]).center(width, '-'))

    # Print the list backwards and then originally skipping the first line (center line)
    print('\n'.join(L[::-1] + L[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)