def print_numbers(m):
    print(*range(m, -1, -1), sep='\n')

if __name__ == "__main__":
    m = 10
    print_numbers(m)
