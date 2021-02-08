def personal_data(name, surname, b_year, town, email, phone):
    """
    displays the entered personal data in the form of a string
    :param name: first name (str)
    :param surname: family name (str)
    :param b_year: the year of birth (int)
    :param town: home town
    :param email: personal email (str)
    :param phone: mobile phone (str)
    :return: str
    """
    print(f'{name} {surname} {b_year} года рождения, город проживания: {town}, '
          f'email: {email}, моб. телефон: {phone}')


personal_data(name='Nastya', surname='Okhtienko', b_year=1999, town='Moscow',
              phone='123-45-67', email='abc@mail.ru')
