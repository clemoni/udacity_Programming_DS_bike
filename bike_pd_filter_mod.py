import pandas as pd
import numpy as np
from datetime import datetime


def convert_city(city):
    """convert str city to csv file name
    Args:
        city ([str]): a chosen city

    Returns:
        [str]: the csv name related to the city
    """
    if city == 'new york':
        city = city.replace(' ', '_')
        city += '_city'
    return city


def get_city_csv(city):
    """generate a path to file based of a given csv file name

    Args:
        city ([str]): csv file name

    Returns:
        [str]: path to a give csv file 
    """
    path_to_file = './data/{city}.csv'.format(city=city)
    return pd.read_csv(path_to_file)


def trim_df(df, *cols):
    """Removed unwanted column to a DataFrame

    Args:
        df ([DataFrame]): a dataFrame

    Returns:
        [list]: list of columns name 
    """
    len_col_origin = len(df.columns)
    for col in cols:
        del df[col]
    len_col_trimed = len(df.columns)

    if len_col_origin > len_col_trimed:
        return '{del_col} column(s) deleted'.format(del_col=len_col_origin - len_col_trimed)


def convert_month_to_digit(month):
    """return the corresponding digit to a given month

    Args:
        month ([str]): a given month

    Returns:
        [int]: digit correspondign to month
    """
    return int(datetime.strptime(month, '%B').strftime('%m').strip('0'))


def df_filter_per_month(df, month):
    """filter a dataFrame according to a given month

    Args:
        df ([DataFrame]): a given dataFrame
        month ([str]): a given month

    Returns:
        [dataFrame]: the filtered dataFrame
    """
    return df[df.index.month == convert_month_to_digit(month)]


def day_to_digit(day):
    """return the corresponding digit to a given day

    Args:
        month ([str]): a given day

    Returns:
        [int]: digit correspondign to day
    """
    day_of_week = ('monday', 'tuesday', 'wednesday',
                   'thursday', 'friday', 'saturday', 'sunday')
    return day_of_week.index(day)


def df_filter_per_day(df, day):
    """filter a dataFrame according to a given day

    Args:
        df ([DataFrame]): a given dataFrame 
        month ([str]): a given day

    Returns:
        [dataFrame]: the filtered dataFrame 
    """
    return df[df.index.dayofweek == day_to_digit(day)]


def filt_time_period(df, filter_choice):
    """Depeding of choice user made in filter_choice
    filters a dataFrame by month, day or not

    Args:
        df ([dataFrame]): a given dataFrame
        filter_choice ([dict]): Dictionnary of filters made by user

    Returns:
        [dataFrame]: the filtered dataFrame
    """
    if 'time' in filter_choice.keys():
        filter_time_type = filter_choice['time']
        chosen_time_add = filter_choice['time_add']

        if filter_time_type == 'day':
            df = df_filter_per_day(df, chosen_time_add)

        elif filter_time_type == 'month':
            df = df_filter_per_month(df, chosen_time_add)

    return df


def main():
    city = 'chicago'
    df = get_city_csv(convert_city(city))
    print(df)


if(__name__ == '__main__'):
    main()
