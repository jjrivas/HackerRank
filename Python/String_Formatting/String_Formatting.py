def print_formatted(number):
    width = len('{0:b}'.format(number))
    for i in range(1, number + 1):
        # {0:... refers to indice in format()}
        # {:{width}...} allows for specification of width of string
        # {:{}d/o/X/b} allows for specification of number format
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width = width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)