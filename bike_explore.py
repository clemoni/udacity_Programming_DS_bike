import pandas as pd
import numpy as np
from datetime import datetime
from bike_form_module import is_valid_choice_recurcive as is_valid_choice
import bike_pd_filter_mod as bf


pd.set_option('display.max_colwidth', None)


filter_choice = is_valid_choice()


####### FILTER DF ACCORDING TO USER ANSWER ######
city_name = bf.convert_city(filter_choice['city'])
df = bf.get_city_csv(city_name)

# remove unwanted column
bf.trim_df(df, 'Unnamed: 0', 'End Time')

# convert col 'Start Time' to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])
# # set col 'Start Time' to be able to slice it depending of filter
df = df.set_index('Start Time').sort_index()

# filter df according to user choice
df = bf.filt_time_period(df, filter_choice)


# Print
message = '\nHere some information based on you filter for the city of {city}\n'.format(
    city=filter_choice['city'].title())
print(message)


############################
#1 Popular times of travel#
s_most_month = (df.index.month_name().value_counts().reset_index().max())
s_most_day = (df.index.day_name().value_counts().reset_index().max())
most_hour = (df.index.hour.value_counts().reset_index().loc[0, 'index'])
data = {'Month': [s_most_month['index']],
        'Day': [s_most_day['index']],
        'Hour': [most_hour]
        }

df_times_travel = pd.DataFrame(data, index=['Most Frequent'])
print('Popular times of travel:')
print(df_times_travel)

#############################
#2 Popular stations and trip#
data = dict()
data['Start Station'] = df['Start Station'].mode()[0]
data['End Station'] = df['End Station'].mode()[0]
# print(df['End Station'].value_counts())
df['Station Start/End'] = df['Start Station'] + ' || ' + df['End Station']
data['Station Start/End'] = df['Station Start/End'].mode()[0]
df_station = pd.DataFrame(data=data, index=['Most Frequent'])

# col = {'Most Frequent': [df['Start Station'].mode()[0], df['End Station'].mode()[
#     0], df['Station Start/End'].mode()[0]]}
# ind_list = ['Start Station', 'End Station', 'Station Start/End']
# df_station = pd.DataFrame(data=col, index=ind_list)
print('\nPopular stations and trip:')
print(df_station)

#################
#3 Trip duration#
data = {"Trip Duration": [
    df['Trip Duration'].sum(), df['Trip Duration'].mean()]}
index_df = ['Total travel time', 'Average travel time']
df_trip_duration = pd.DataFrame(data=data, index=index_df)
print('\nTrip duration:')
print(df_trip_duration)
######################################
##########  4.1 USER COUNT  ##########

tot_user_type = df['User Type'].count()
user_count = df['User Type'].value_counts()
df_user_count = user_count.to_frame(name='Count')
df_user_count['Percent'] = user_count/tot_user_type*100
df_user_count.index.name = 'User Type'
print('\nUser Count:')
print(df_user_count)

if filter_choice['city'] == 'chicago' or filter_choice['city'] == 'new york':
    #######################################
    #########  4.2 GENDER COUNT  ##########
    # (only available for NYC and Chicago)#

    tot_gender = df['Gender'].count()
    gender_count = df['Gender'].value_counts()
    df_gender_count = gender_count.to_frame(name='Count')
    df_gender_count['Percent'] = gender_count/tot_gender*100
    df_gender_count.index.name = 'Gender'
    print('\nGender Count:')
    print(df_gender_count)

    #######################################
    ##########  4.3 DOB COUNT  ############
    # (only available for NYC and Chicago)#
    yob_min = int(df['Birth Year'].min())
    yob_max = int(df['Birth Year'].max())
    yob_mod = int(df['Birth Year'].mode())
    age = 2017 - df['Birth Year']
    yob_age_mean = round(age.mean())
    data = {'Value': [yob_min, yob_max, yob_mod, yob_age_mean]}
    df_yob = pd.DataFrame(
        data=data, index=['Min', 'Max', 'Most Frequent', 'Mean Age'])
    print('\nYear of birth:')
    print(df_yob)
