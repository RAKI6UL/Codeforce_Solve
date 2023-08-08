def subtract(R, S):
    for _ in range(S):
        if R % 10 == 0:
            R //= 10
        else:
            R -= 1
    return R

R, S = map(int, input().split())

result = subtract(R, S)
print(result)
