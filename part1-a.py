
def find_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1
        sequence.append(n)
    return sequence

print(find_sequence(13))


