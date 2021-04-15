import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('\n Please enter a city name or number from: 1. Chicago 2. New york city 3. Washington \n').lower()
    #while city.lower() not in CITY_DATA and city not in range(1,4):
    while True:
        if city == '3':
            city = 'washington'
            break
        if city == '2':
            city = 'new york city'
            break
        if city == '1':
            city = 'chicago'
            break
        if city not in CITY_DATA:
            city=input('\n Please enter a city name or number from the three given cities as listed:  ').lower()
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['January','February','March','April','May','June']

    month=input('\n Please enter a month name or number from: 1. January 2. February 3. March 4. April 5. May 6. June \n').title()
    while True:
        if month in ['1','2','3','4','5','6']:
            month=months[int(month)-1]
            break
        if month not in months:
            month=input('\n Please enter a month name or number from the six given months as listed:  ').title()
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    day=input('\n Please enter a day name or number from: 1. Monday 2. Tuesday 3. Wednesday 4. Thursday 5. Friday 6. Saturday 7. Sunday \n').title()
    while True:
        if day in ['1','2','3','4','5','6','7']:
            day=days[int(day)-1]
            break
        if day not in days:
            day=input('\n Please enter a month name or number from the seven given days as listed:  ').title()
        else:
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
    df=pd.read_csv("bikeshare-datasets/{}".format(CITY_DATA[city]))
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    #df['month'] = df['Start Time'].dt.month                #.month returns months represented from 1 addressed for January
    df['month'] = df['Start Time'].dt.month_name()

    #df['day_of_week'] = df['Start Time'].dt.weekday        #.weekday returns days represented from 0 addressed for Monday
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    x=input('To filter by the entered month input "Y", to proceed without filtering by month enter any thing else: \n').lower()
    if x=='y':
        #df = df[ df['month'] == (1 + months.index(month))]
        df = df[ df['month'] == month]
    # filter by day of week if applicable
    y=input('To filter by the entered day input "Y", to proceed without filtering by day enter any thing else: \n').lower()
    if y=='y':
        #df = df[df['day_of_week'] == days.index(day)]
        df = df[df['day_of_week'] == day]
    #print(df)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].mode()[0]
    #print('The most common month is: \n', months[int(common_month)-1])      #months are represented from 1 in the dataFrame column
                                                                            #the month index in the global months list index starts from month-1                                                                          
    print('The most common month is: \n', common_month)
    # display the most common day of week
    common_day=df['day_of_week'].mode()[0]

    #print('The most common day is: \n', days[int(common_day)])      #days are represented from 0 in the dataFrame column                                                                                    
    print('The most common day is: \n', common_day)                                                                #the day index in the global days list index starts from day
    
    # display the most common start hour
    common_start_hour=df['Start Time'].dt.hour.mode()[0]
    print('The most common hour is: \n', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common start station is: \n', df['Start Station'].mode()[0] )

    # display most commonly used end station
    print('The most common end station is: \n', df['End Station'].mode()[0] )

    # display most frequent combination of start station and end station trip
    print('The most frequent combination is: \n', (df['Start Station'] +' - '+ df['End Station']).mode()[0])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_seconds=df['Trip Duration'].sum()
    y= total_seconds//(60*60*24*365)
    mnth= (total_seconds % (60*60*24*365)) //(3600*24*30)
    d= ((total_seconds % (60*60*24*365))%(3600*24*30))//(3600*24)
    h= (((total_seconds % (60*60*24*365))%(3600*24*30))%(3600*24)) // 3600
    m=((((total_seconds % (60*60*24*365))%(3600*24*30))%(3600*24)) % 3600) //60
    s=(((((total_seconds % (60*60*24*350))%(3600*24*30))%(3600*24)) % 3600)) %60
    print(f'The total travel time is {y} year(s),{mnth} month(s), {d} day(s), {h} hour(s), {m} minute(s) and {s} second(s).\n','With total seconds = {} \n'.format(total_seconds) )

    # TO DO: display mean travel time
    #print('The mean travel time is: \n', df['Trip Duration'].mean() )
    Average=df['Trip Duration'].mean()
    #y= Average//(60*60*24*365)
    #mnth= (Average % (60*60*24*365))//(3600*24*30*12)
    d= ((Average % (60*60*24*365))%(3600*24*30))//(3600*24)
    h= (((Average % (60*60*24*365))%(3600*24*30))%(3600*24)) // 3600
    m=((((Average % (60*60*24*365))%(3600*24*30))%(3600*24)) % 3600) //60
    s=(((((Average % (60*60*24*365))%(3600*24*30))%(3600*24)) % 3600)) %60
    print(f'The average travel time is {d} day(s), {h} hour(s), {m} minute(s) and {s} second(s).\n','With total average of {} seconds\n'.format(Average))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts(),'\n')

    try:
        # Display counts of gender
        print(df['Gender'].value_counts(),'\n')
        
        # Display earliest, most recent, and most common year of birth
        print('Earliest birth year: ', df['Birth Year'].min())
        print('Most recent birth year: ', df['Birth Year'].max())
        print('Most common birth year: ', df['Birth Year'].mode()[0])
    except:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(city):
    """ Offers to load five rows of raw data for the specified city """

    df=pd.read_csv("bikeshare-datasets/{}".format(CITY_DATA[city]))
    print('Row Data descriptive statistics: \n', df.describe())
    raw_index = 0
    message=input('\n To see 5 lines of raw data press "Y", otherwise to skip. >>' ).lower()
    while True:
        if message=='y':
            print(df[raw_index:raw_index+5])
            raw_index+=5
            message=input('\n To see more 5 lines of raw data press "Y", otherwise to skip. >>').lower()
        else:
            break
        
def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            raw_data(city)

            restart = input('\nWould you like to restart? Enter yes, otherwise to exit.\n')
            if restart.lower() != 'yes':
                break
        except:
            pass

if __name__ == "__main__":
	main()
