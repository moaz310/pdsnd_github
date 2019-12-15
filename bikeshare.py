import time
import pandas as pd
import numpy as np

#Data set

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city, month, day = '', '', ''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('please enter the city you want to analize type one of (chicago, new york city, washington)')
        city = input().lower()
        if city not in CITY_DATA.keys():
            print('Please enter valid data')
            continue
        print('please enter the month to filter by (all, january, february, ... , june)')
        month = input().lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('Please enter valid data')
            continue
        print('please enter the day to filter by (all, monday, tuesday, ... sunday)')
        day = input().lower()
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('Please enter valid data')
            continue
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    print('the most common month is', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('the most common day', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('the most common start hour', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most commonly used start station is: ', df['Start Station'].mode()[0]) 

    # TO DO: display most commonly used end station
    print('the most commonly used end station is: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('the most commonly used start station and end station trip station is: ', (df['Start Station'] + ' ' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('the total time travel', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('the average travel time', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('the number of user types', df['User Type'].value_counts())

    # TO DO: Display counts of gender

    if 'Gender' in df:
        print('the count of gender', df['Gender'].value_counts())
    else:
        print('no Gender in the data')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('the earliest year is:', df['Birth Year'].min(), 'the most recent year is: ', df['Birth Year'].max(), 'the common year is: ', df['Birth Year'].mode()[0])
    else:
        print('no Birth Year in the data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        n = 5
        print(df.head(n))
        while True:
            more_data = input('\nwould you like to show more data please enter yes or no\n')
            if more_data.lower() != 'yes':
                break
            n += 5
            print(df.head(n))
            
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
