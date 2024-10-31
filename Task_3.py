def print_numbers(m):
    print(m)
    m > 0 and print_numbers(m - 1)

if __name__ == "__main__":
    m = 10
    print_numbers(m)
