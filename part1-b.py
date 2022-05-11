def find_largest_sequence(n):
    temp = {number: 0 for number in range(1, n)}
    temp[1] = 1
    temp[2] = 2
    for value in range(3, n):
        counter = 0
        current = value
        while value > 1:
            if value < current:
                temp[current] = temp[value] + counter
                break
            if value%2 == 0:
                value = value/2
                counter += 1
            else:
                value = 3*value + 1
                counter += 1
    return list(temp.values()).index(max(temp.values()))+1

print(find_largest_sequence(13))
