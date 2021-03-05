class NotNumberError(Exception):
    def __init__(self, message):
        self.message = message

    @staticmethod
    def valid_number(number):
        try:
            return True if float(number) else True
        except ValueError:
            return False


def main():
    numbers_list = []
    while True:
        number = input('Input. Enter "stop" to break: ').strip().split(' ')
        for i in number:
            if i == 'stop':
                print(numbers_list)
                return False
            try:
                if NotNumberError.valid_number(i):
                    numbers_list.append(float(i))
                else:
                    raise NotNumberError("Please enter only numbers  or 'stop'!")
            except NotNumberError as ex:
                print(ex)
                continue
        print(numbers_list)


if __name__ == '__main__':
    main()
