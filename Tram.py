# Read the number of stops
n = int(input())

current_passengers = 0
min_capacity = 0

for _ in range(n):
    exiting, entering = map(int, input().split())
    
    current_passengers -= exiting
    current_passengers += entering
    
    min_capacity = max(min_capacity, current_passengers)

print(min_capacity)
