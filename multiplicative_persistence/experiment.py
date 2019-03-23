def recursive_persistence(number, base, sequence):
    sequence.append(number)
    next_number = 1
    quotient = number
    while quotient != 0 and next_number != 0:
        (quotient, remainder) = divmod(quotient, base)
        next_number *= remainder
    if number != next_number and number != 0:
        recursive_persistence(number=next_number, base=base, sequence=sequence)


def persistence(number, base):
    sequence = []
    recursive_persistence(number=number, base=base, sequence=sequence)
    return sequence


def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)


def str_base(number, base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)


for base in xrange(2, 15):
    longest_sequence = []
    for number in xrange(10 ** 6):
        sequence = persistence(base, number)
        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence
    length = len(longest_sequence)
    sequence = [str_base(i, base) for i in longest_sequence]
    print("Base {base}, length {length}, sequence {sequence}".format(base=base, length=length, sequence=sequence))
