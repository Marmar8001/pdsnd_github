import time
import pandas as pd
import numpy as np
# make dictionary from city data files

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city= input("Enter the city name you are looking for in US: ")
        if city not in ["Chicago", "New York City", "Washington"]:
            print( "No data available for this city. please choose another city")
            continue
        else:

            break

    # get user input for months. HINT: Use a while loop to handle invalid inputs

    months=["January", "February","March",  "April",  "May", "June", "all"]
    while True:

        month= input("Enter the month you are looking for: ")
        if month not in months:
            print( "No data available for this month. please choose another month")
            continue
        else:
            break

    days_of_week=["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday", "all"]
    while True:
        day= input("Enter the week day you are looking for: ")
        if day not in days_of_week:
            print( "No data available for this day. please choose another day")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return (df)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    print("most common month: ",(df['month'].mode()[0]))


    # display the most common day of week

    print("most common day of week: ",(df['day'].mode()[0]))



    # display the most common start hour

    df['hour']= df['Start Time'].dt.hour
    print("most common start hour: ",(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("most common start station: ",(df['Start Station'].mode()[0]))


    # display most commonly used end station
    print("most common end station: ", (df["End Station"].mode()[0]))

    # display most frequent combination of start station and end station trip

    print("most frequent combination of start and end station: ",((df['Start Station']+df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total travel time: ",(df['Trip Duration'].sum()))


    # display average travel time
    print("mean travel time: ", (df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("counts of user type: ",(df['User Type'].value_counts()))



    # Display counts of gender.Some data files does not have date of birth or gender type
    try:
        print("counts of gender:",(df['Gender'].value_counts()))
    except KeyError:
        print("No data available")


    # Display earliest, most recent, and most common year of birth
    try:
        print("earliest year of birth: ",(df['Birth Year'].min()))
    except KeyError:
        print("No data available")

    try:
        print("most recent year of birth: ",(df['Birth Year'].max()))
    except KeyError:
        print("No data available")

    try:
        print("most common year of birth: ",(df['Birth Year'].mode()))
    except:
        print("No data available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def display_raw_data(df):
    """ Display raw data upon user request"""
    count=0
    while True:
        raw_data=input("Do you want to see raw data? Answer with yes or No ")
        if (raw_data=="yes"):
            print(df.iloc[count:(count+5)])
        elif (raw_data=="No"):
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
