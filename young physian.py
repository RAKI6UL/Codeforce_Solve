def is_equilibrium(n, forces):
    total_force = [0, 0, 0]
    
    for force in forces:
        total_force[0] += force[0]
        total_force[1] += force[1]
        total_force[2] += force[2]
    
    if total_force == [0, 0, 0]:
        return "YES"
    else:
        return "NO"

# Read input
n = int(input())
forces = []
for _ in range(n):
    x, y, z = map(int, input().split())
    forces.append((x, y, z))

# Check equilibrium and print result
result = is_equilibrium(n, forces)
print(result)
