import math


# construct a progress bar
def construct_bar(progress, total):
    rate = progress / total
    res = '【'
    dots = math.floor(20 * rate)
    for i in range(dots):
        res += '*'
    for i in range(20 - dots):
        res += '-'
    return res + '】'


print(construct_bar(80, 100))




