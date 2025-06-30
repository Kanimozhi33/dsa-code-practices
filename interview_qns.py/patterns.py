def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()
   
full_pyramid(5)

def print_space(space):
    if space > 0:
        print(" ", end="")
        print_space(space - 1)

def print_star(star):
    if star > 0:
        print("*", end="")
        print_star(star - 1)

def print_pyramid(n, current_row=1):
    if current_row > n:
        return

    spaces = n - current_row
    stars = 2 * current_row - 1

    # Print spaces
    print_space(spaces)

    # Print stars
    print_star(stars)

    # Move to the next line for the next row
    print()

    # Print the pyramid for the next row
    print_pyramid(n, current_row + 1)

# Set the number of rows for the pyramid
n = 5

# Print the pyramid pattern
print_pyramid(n)