import re


def term_eval(input):

    # handle ()
    exprs = re.findall("(\(.*\))", input)
    if exprs:
        expr = exprs[0]
        expr_stripped = expr[1:-1]

        res = eval(expr_stripped)
        input = input.replace(expr, str(res))

        return eval(input)

    # handle /
    divs = re.findall("-?\d+\/-?\d+", input)
    if divs:
        div = divs[0]
        nums = div.split("/")

        res = int(int(nums[0]) / int(nums[1]))
        input = input.replace(div, str(res))

        return eval(input)

    # handle *
    divs = re.findall("-?\d+\*-?\d+", input)
    if divs:
        div = divs[0]
        nums = div.split("*")

        res = int(int(nums[0]) * int(nums[1]))
        input = input.replace(div, str(res))

        return eval(input)

    # handle -
    divs = re.findall("-?\d+\--?\d+", input)
    if divs:
        nums = divs[0]

        vals = re.findall("(-?\d+)\-(-?\d+)", nums)
        val = vals[0]

        res = int(int(val[0]) - int(val[1]))
        input = input.replace(nums, str(res))

        return eval(input)

    # handle +
    divs = re.findall("-?\d+\+-?\d+", input)
    if divs:
        div = divs[0]
        nums = div.split("+")

        res = int(int(nums[0]) + int(nums[1]))
        input = input.replace(div, str(res))

        return eval(input)

    try:
        int(input)
        return input
    except:
        return eval(input)
