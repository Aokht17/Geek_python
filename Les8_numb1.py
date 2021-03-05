class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def str_to_int(cls, date):
        return [int(i) for i in date.split("-")]

    @staticmethod
    def date_validation(param):
        valid = Data.str_to_int(param)
        year_dict = {1: 31, 2: None, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if (valid[2] % 4) == 0:
            if (valid[2] % 100) == 0:
                if (valid[2] % 400) == 0:
                    year_dict[2] = 29
                else:
                    year_dict[2] = 28
            else:
                year_dict[2] = 29
        else:
            year_dict[2] = 28
        try:
            if isinstance(valid[0], int) and year_dict[valid[1]] >= valid[0] > 0:
                print(f'Day: {valid[0]}')
            else:
                print(f'{valid[0]} is wrong format of a day')
        except KeyError:
            pass

        if isinstance(valid[1], int) and 12 >= valid[1] > 0:
            print(f'Month: {valid[1]}')
        else:
            print(f'{valid[1]} is wrong format of a month')

        if isinstance(valid[2], int):
            print(f'Year: {valid[2]}')
        else:
            print(f'{valid[2]} is wrong format of a year')


Data.date_validation('10-01-1999')
Data.date_validation('01-23-2000')
Data.date_validation('29-02-2020')
Data.date_validation('29-02-2021')
