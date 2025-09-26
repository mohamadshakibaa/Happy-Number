def is_happy(n):
    seen_number = set()
    while (n != 1) and (n not in seen_number):
        seen_number.add(n)
        n = sum([int(number) ** 2 for number in str(n)])
    
    return n == 1

num = input("Enter a number: ")
print(is_happy(num))