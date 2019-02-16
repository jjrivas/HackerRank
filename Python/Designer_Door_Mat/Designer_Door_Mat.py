# Enter your code here. Read input from STDIN. Print output to STDOUT
# Specs of door mat:
# - Must be size N x M (N is an odd natural number, and M is 3 times N)
# - The design should have 'WELCOME' written in the center
# - The design pattern should only use |, . and - characters.

def print_ends(N, M, r_start, r_stop, r_step) :
    dash = '-'
    dot_line = '.|.'

    for i in range(r_start, r_stop, r_step):
        print((dash * int(((M - 3) / 2) - (3 * i))), end='')
        print(dot_line * (i * 2 + 1), end='')
        print((dash * int(((M - 3) / 2) - (3 * i))))

def print_mat(N, M):
    dash = '-'

    print_ends(N, M, 0, N // 2, 1)
    print(dash * int((M - 7) / 2) + 'WELCOME' + dash * int((M - 7) / 2))
    print_ends(N, M, N // 2 - 1, -1, -1)

if __name__ == "__main__":
    # Get dimensions from user
    N, M = map(int, input().split())

    # Validate inputs
    if((N % 2 == 0) or (N * 3 != M)):
        print("Invalid input: First number must be odd."
              " Second number must be three times as large as first number.")
        exit()    
    
    # Short way
    pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
    print("\n".join(pattern + ['WELCOME'.center(M, '-')] + pattern[::-1]))
    exit()

    # Long way
    print_mat(N, M)