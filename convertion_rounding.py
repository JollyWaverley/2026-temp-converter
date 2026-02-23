def round_ans(val):

    """Round the temperatures to teh nearest degree
    :param val Number would be rounded
    :return: Number to nearest degree"""

    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)

def to_celsius(to_convert):
    """Converts from f to c
    param to_convert : temperature to be converted into f
    :return: Converted in c"""

    answer = (to_convert - 32) * 5 / 9
    return round_ans(answer)


def to_fahrenheit(to_convert):
    """
    Converts from c to f
    : param to_ convert : temperature to be in c
    : return : Converted temperature in f
    """
    answer = to_convert * 1.8 + 32
    return  round_ans(answer)