def positive_negative_zero(num):
    positive = []
    negative = []
    zero = []

    for i in num:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        else:
            zero.append(i)

    return positive, negative, zero


num = [40, -45, 8, 0, -4, 0]

positive, negative, zero = positive_negative_zero(num)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)