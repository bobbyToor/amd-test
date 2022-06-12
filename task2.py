import sys


def main(input):

    for i in range(len(input) - 1, 0, -1):

        d2 = int(input[i])
        d1 = int(input[i - 1])

        if d1 > d2:
            d1 = d1 - 1
            d2 = 9

            digit_list = list(input)

            digit_list[i] = str(d2)
            digit_list[i - 1] = str(d1)

            for j in range(i, len(digit_list)):
                digit_list[j] = "9"

            input = "".join(digit_list)

    print(int(input))


main((sys.argv[1]))
