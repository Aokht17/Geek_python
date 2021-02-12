from sys import argv

name, working_out, rate, award = argv
working_out, rate, award = float(working_out), float(rate), float(award)


def count_salary(working_out, rate, award):
    """
    counts the salary including working out and additional award

    """
    return working_out * rate + award


print(count_salary(working_out, rate, award))
