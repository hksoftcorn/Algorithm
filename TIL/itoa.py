def itoa(num):
    def digit_length(num):
        count = 0
        while num:
            num //= 10
            count += 1
        return count

    count = digit_length(num)
    value = ''
    for i in range(count - 1, -1, -1):
        num_int = num // (10 ** i)
        num -= num_int * (10 ** i)
        value += chr(num_int + 48)
    return value

num = 123
print(itoa(num))