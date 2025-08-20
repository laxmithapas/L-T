


num = int(input("Enter a number: "))


seen = set()


while num != 1 and num not in seen:
    seen.add(num)
    sum_of_squares = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_squares += digit ** 2
        temp = temp // 10
    num = sum_of_squares


if num == 1:
    print("Happy Number ✅")
else:
    print("Not a Happy Number ❌")
