import sys
from termer import term_eval


def main(input):
    input = input.replace(" ", "")

    return term_eval(input)


print(main((sys.argv[1])))
