def distinct_digits(year):
    digits = set()
    while year > 0:
        digit = year % 10
        if digit in digits:
            return False
        digits.add(digit)
        year //= 10
    return True

def next_distinct_year(year):
    year += 1
    while not distinct_digits(year):
        year += 1
    return year

y = int(input()) 
next_year = next_distinct_year(y) 
print(next_year)  
