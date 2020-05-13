import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_city():
    """
    Prompt user to specify a city to analyze.
    Returns:
        (str) filename from bikeshare data of a city to analyze.
    """
    print('Hello! Let\'s explore some US bikeshare data!\nFollow the prompts for guided exploration.\nLet\'s begin!\n')
    # Specify one of three cities: Chicago, New York City, and Washington.
    while True:
        try:
            city = input('Would you like to explore Chicago, New York City, or Washington?\n').title()
            if city == 'Chicago' or city == 'chicago':
                return 'chicago.csv'
            elif city == 'New York City' or city == 'new york city':
                return 'new_york_city.csv'
            elif city == 'Washington' or city == 'washington':
                return 'washington.csv'
            else:
                print('City names include: Chicago, New York City, or Washington.')
        except ValueError:
            print('City names include: Chicago, New York City, or Washington.')
    return city


def get_month():
    """
    Prompt user to speficy a month to explore.
    Returns:
        (str) Convert month into number.
    """
    # Speficy the month between January and June.
    while True:
        try:
            month = input('Enter the month you wish to explore.\n')
            if month != 'all':
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                month = months.index(month)
                break
        except ValueError:
            print('Month options are from January to June written in lowercase letters.')


def get_day():
    """
    Prompt user to speficy a day of the week to explore.
    Returns:
        (int) Day of the week as an integer.
    """
    # Speficy the day of the week.
    while True:
        try:
            day = input('Enter the day you wish to explore.\n')
            if day != 'all':
                days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
                day = days.index(day)
                break
        except ValueError:
            print('Days of the week should be entered using lowercase letters.')


def popular_month(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the most popular month traveled.
    Args:
        df: DataFrame of bikeshare data
    Returns:
        (str) Month with most traveled trips.
    """
    # Display the most popular month traveled.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    popular_month = df['month'].mode()
    print('The most popular month taveled is {}.\n'.format(popular_month).replace('0   ', ''))


def popular_day(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the most popular day traveled.
    Args:
        df: DataFrame of bikeshare data
    Returns:
        (str) Day with most traveled trips.
    """
    # Display the most popular day of the week traveled.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()
    print('The most popular day of the week traveled is{}.\n'.format(popular_day).replace('0   ', ''))



def popular_hour(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the most popular hour traveled.
    Args:
        df: DataFrame of bikeshare data
    Returns:
        (str) Hour with most traveled trips.
    """
    # Display the most popular start hour traveled.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour to start to travel is {}.\n'.format(popular_hour).replace('0   ', ''))



def popular_stations(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the most popular stations visited.
    Args:
        df: DataFrame of bikeshare data
    Returns:
        (str) Most popular starting station
        (str) Most popular ending station
    """
    # Display most commonly used start station.
    popular_start_station = df['Start Station'].mode()
    print('The most commonly used start station is\n{}.\n'.format(popular_start_station).replace('0', ''))

    # Display most commonly used end station.
    popular_end_station = df['End Station'].mode()
    print('The most commonly used end station is\n{}.\n'.format(popular_end_station).replace('0', ''))



def popular_trip(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the most popular trips.
    Args:
        df: DataFrame of bikeshare data
    Returns:
        (str) Most popular combination of starting and ending stations with a count and percentage or total trips.
    """
    # Display most frequent combination of start station and end station trips.
    popular_start_end_stations = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(1)
    print('The most commonly used start and end station is\n{}.\n'.format(popular_start_end_stations))



def trip_duration(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the total trip duration and average trip duration.
    Args:
        df: DataFrame of bikeshare data
    Returns:
        (str) Total trip duration in years, days, hours, minutes, & seconds
        (str) Average trip duration in hours, minutes, & seconds
    """
    # Calculate the total trip time and the average trip time.
    total_trip_dur = df['Trip Duration'].sum()
    print('The total time traveled was {}.\n'.format(total_trip_dur))
    avg_trip_dur = df['Trip Duration'].mean()
    print('The average travel time was {}.\n'.format(avg_trip_dur))



def user_stats(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return a count of trips by user type and gender (if applicatble).
    Args:
        df: DataFrame of bikeshare data
    Returns:
        (panda series) Two series...
            First series: User type count of trips
            Second series: Gender count of trips
        (list) Three string values...
            First value: Earliest birth year of users
            Second value: Most recent birth year of users
            Third value: Most common birth year of users
    """

    # Display counts of user types
    if 'User Type' in df.columns:
        user_type = df['User Type'].value_counts()
        print('The total amount of each user type is:\n{}\n'.format(user_type))

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('The total amount of each gender is:\n{}\n'.format(gender))
    except:
        print('There is no gender information for Washington.\n')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = min(df['Birth Year'])
        print('The earliest birth year is {}.\n'.format(earliest_birth_year))
        recent_birth_year = max(df['Birth Year'])
        print('The most recent birth year is {}.\n'.format(recent_birth_year))
        common_birth_year = df['Birth Year'].mode()
        print('The most common birth year is{}.\n'.format(common_birth_year).replace('0   ', ''))

    except:
        print('There is no birth year information for Washington.\n')


def display_data(df):
    """
    Call users to view 5 rows of data. Ask if they would like to repeat call.
    Args:
        df: DataFrame of bikeshare data
    Returns:
        (list) Five rows of data
    """
    # Prompt to see 5 rows of data.  Once returned, prompt for 5 more rows of data.
    counter = 0
    user_input = input('\nWould you like to see five lines of raw data? Type yes or no.\n').lower()
    while True :
        if user_input != 'no':
            print(df.iloc[counter : counter + 5])
            counter += 5
            user_input = input('\nWould you like to see five more lines of raw data? Type yes or no.\n')
        else:
            break


def main():
    """
    Calculations & printouts of the statistics specified by the user of a city and time period.
    """
    # Filter by city (Chicago, New York City, Washington)
    while True:
        city = get_city()
        month = get_month()
        day = get_day()
        df = pd.read_csv(city, month, day)

        # Prompt user to view 5 rows of raw data.
        display_data(df)
        # Display filtered data.
        popular_month(df)
        popular_day(df)
        popular_hour(df)
        popular_stations(df)
        popular_trip(df)
        trip_duration(df)
        user_stats(df)

        break


    # Prompt user to restart filters
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() == 'yes':
        return main()
    restarts = input('\nAre you sure you want to leave?\n')
    if restarts.lower() == 'yes':
        print('\nCome back later!')
    elif restarts.lower() == 'no':
        return main()


if __name__ == "__main__":
    main()
