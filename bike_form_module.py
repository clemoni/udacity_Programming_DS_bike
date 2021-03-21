# Would you like to see data for Chicago, New York, or Washington?
# Would you like to filter the data by month, day, or not at all?
# (If they chose month) Which month - January, February, March, April, May, or June?
# (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?


def what_city(cities=('chicago', 'new york', 'washington')):
    """Recurcive input - Ask user to pick city from given cities

    Args:
        cities (tuple, optional):Do not modified, value tested. 
        Defaults to ('chicago', 'new york', 'washington').

    Raises:
        ValueError: No information given EMPTY
        ValueError: value given does not correspond to citites tuple

    Returns:
        [string]: valid input
    """
    try:
        original_value = str(
            input('\nWould you like to see data for Chicago, New York, or Washington? ')).strip()
        test_value = original_value.lower()
        if not test_value:
            raise ValueError('No answer given')
        if test_value not in cities:
            raise ValueError(
                f'The value you entered ({original_value}) does not correspond to the expected city.')
    except Exception as e:
        print(e)
        return what_city()
    else:
        print(f'\nYou chose the following city: {original_value}\n')
        return test_value


def what_time(time=('month', 'day', 'not at all')):
    """Recurcive input - Ask user to pick time from given time period

    Args:
        time (tuple, optional): Do not modified, value tested.. 
        Defaults to ('month', 'day', 'not at all').

    Raises:
        ValueError: No information given EMPTY
        ValueError: value given does not correspond to time period tuple

    Returns:
        [string]: valid input
    """
    try:
        original_value = str(
            input('\nWould you like to filter the data by month, day, or not at all? ')).strip()
        tested_value = original_value.lower()
        if not tested_value:
            raise ValueError('No answer given')
        if tested_value not in time:
            raise ValueError(
                f'The value you entered ({original_value}) does not correspond to time offered.')
    except Exception as e:
        print(e)
        return what_time()
    else:
        print(f'\nYou chose the following time: {original_value}\n')
        return original_value


def what_month(months=('january', 'february', 'march', 'april', 'may', 'june')):
    """Recurcive input - Ask user to pick month from given months

    Args:
        months (tuple, optional): Do not modified. 
        Defaults to ('january', 'february', 'march', 'april', 'may', 'june').

    Raises:
        ValueError: No information given EMPTY
        ValueError: value given does not correspond to months tuple

    Returns:
        [string]: [description]
    """
    try:
        original_value = str(
            input('\nWhich month - January, February, March, April, May, or June? ')).strip()
        tested_value = original_value.lower()
        if not tested_value:
            raise ValueError('No answer given')
        if tested_value not in months:
            raise ValueError(
                f'The value you entered ({original_value}) does not correspond to the given months.')
    except Exception as e:
        print(e)
        return what_month()
    else:
        print(f'\nYou chose the following month: {original_value}\n')
        return original_value


def what_day(days=('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')):
    """Recurcive input - Ask user to pick day from given days

    Args:
        days (tuple, optional): Do not modifed. 
        Defaults to ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday').

    Raises:
        ValueError: No information given EMPTY
        ValueError: value given does not correspond to days tuple

    Returns:
        [string]: valid input
    """
    try:
        original_value = str(
            input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ')).strip()
        tested_value = original_value.lower()
        if not tested_value:
            raise ValueError('No answer given')
        if tested_value not in days:
            raise ValueError(
                f'The value you entered ({original_value}) does not correspond to the given days.')
    except Exception as e:
        print(e)
        return what_day()
    else:
        print(f'\nYou chose the following day: {original_value}\n')
        return tested_value


def is_valid_choice(answers):
    """Recurcive input - tested if answer given is Y or N

    Args:
        answers ([list]): 
        list of choices made by user

    Raises:
        ValueError: No information given EMPTY
        ValueError: value given does not correspond to Y/N tuple

    Returns:
        [string]: valid input
    """
    answers_string = ', '.join(answers)

    try:
        print(f'Here are the filter(s) you chose : {answers_string}\n')
        original_value = str(
            input('Are you satisfied with you choice Y/N? ')).strip()
        tested_value = original_value.upper()
        if not original_value:
            raise ValueError('No answer given')
        if tested_value not in ('Y', 'N'):
            raise ValueError(
                f'The value you entered ({original_value}) does not correspond to eihter Y or N.')
    except Exception as e:
        print(e)
        return is_valid_choice(answers)
    else:
        return tested_value


def is_valid_choice_recurcive():
    """Recurcive input - 
    build dictionnary with choices made
    Restart if user answers N 
    Return dictionary if user confirm choices

    Returns:
        [dict]: dictionnary with all the choice made
    """
    choice_given = dict()

    choice_given['city'] = what_city()

    time = what_time()

    if time != 'not at all':
        choice_given['time'] = time
        if time == 'month':
            choice_given['time_add'] = what_month()
        elif time == 'day':
            choice_given['time_add'] = what_day()

    confirmed_choice = is_valid_choice(choice_given.values())

    if confirmed_choice == 'N':
        print('Ok, let\'s start over!')
        return is_valid_choice_recurcive()
    elif confirmed_choice == 'Y':
        print('Choice confirmed!!\n')
        return choice_given


def main():
    print('testing')
    is_valid_choice_recurcive()


if(__name__ == '__main__'):
    main()
