def sumto(n):
    sum_nums = 0 
    for number in range(1, 7):
        sum_nums = number + sum_nums
    return sum_nums

print(sumto(6))

large_num = [1,2,3,4,5,6]
find_large = 0
for temp in large_num:
    if find_large < temp:
        find_large = temp

print(temp)

def occurances(string, substring):
    string = string.count(substring)
    return string

print(occurances('always look on the bright side of life', 't'))

def multiplier(a,b):
    return (a * b)

print(multiplier(2, 5))