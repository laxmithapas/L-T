

numbers = list(map(int, input("Write numbers with space: ").split()))


biggest = numbers[0]
for n in numbers:
    if n > biggest:
        biggest = n


second_biggest = numbers[0]
for n in numbers:
    if n != biggest and n > second_biggest:
        second_biggest = n

print("Second biggest number is:", second_biggest)
