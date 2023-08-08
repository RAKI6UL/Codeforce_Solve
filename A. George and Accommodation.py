def main():
    n = int(input())  # Number of rooms
    count = 0  # Counter for rooms with available space

    for _ in range(n):
        p, q = map(int, input().split())  # Number of people and room capacity
        if q - p >= 2:  # There should be at least 2 available spots
            count += 1

    print(count)

if __name__ == "__main__":
    main()
