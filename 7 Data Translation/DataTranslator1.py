from MockDatasetMaker import makeDataset
import pandas
import math

data = makeDataset(100)
gearTeethNum = 10 #number of teeth on the gear
teethSeen = 0
analogPullRate =  50 #time frame to average for analog
digitalPullRate = 100 #time frame to average for digital

data = [line.split() for line in data.strip().split('\n')]
dataFrame = pandas.DataFrame(data, columns=["time", "digital_data", "analog_data"]).astype(float)


# Define a function to calculate and set a constant average 'analog_data' for each timeframe of 'x' units
def averageAnalog(dataFrame, time_window):
    
    # Initialize list to store the constant averaged 'analog_data' values
    averaged_analog_data = []
    current_index = 0

    # Iterate through the DataFrame using time windows
    while current_index < len(dataFrame):
        # Define the current time window range
        current_time = dataFrame.loc[current_index, 'time']
        time_window_end = current_time + time_window
        
        # Select rows within the current time window
        window = dataFrame[(dataFrame['time'] >= current_time) & (dataFrame['time'] < time_window_end)]
        
        # Calculate the average for 'analog_data' in the current time window
        avg_value = window['analog_data'].mean()
        
        # Append the average value for each element in the window
        averaged_analog_data.extend([avg_value] * len(window))
        
        # Move the current index forward by the window length
        current_index += len(window)
    
    # Replace 'analog_data' column with the averaged values
    dataFrame['analog_data'] = averaged_analog_data
    
    # Convert the DataFrame back to a list of lists format
    return dataFrame #[['time', 'digital_data', 'analog_data']].values.tolist()



# Define a function to count transitions of 'digital_data' from 0 to 1 within each x-element window
def processHallEffect(dataFrame, timeWindow):
    
    # Initialize list to store the 'teethSeen' counts
    rpms = []
    current_index = 0

    # Iterate through the DataFrame using time windows
    while current_index < len(dataFrame):
        # Define the current time window range
        current_time = dataFrame.loc[current_index, 'time']
        timeWindow_end = current_time + timeWindow
        
        # Select rows within the current time window
        window = dataFrame[(dataFrame['time'] >= current_time) & (dataFrame['time'] < timeWindow_end)]
        
        # Initialize 'teethSeen' for the current time window
        teeth_seen = 0
        rpm = 0
        
        # Count transitions from 0 to 1 in the current window
        for j in range(1, len(window)):
            if window['digital_data'].iloc[j-1] == 0 and window['digital_data'].iloc[j] == 1:
                teeth_seen += 1
        rpm = 60 * teeth_seen / gearTeethNum / timeWindow #ASSUMING time window is measured in Seconds
        
        # Append the count for each element in the window
        rpms.extend([rpm] * len(window))
        
        # Move the current index forward by the window length
        current_index += len(window)
    
    # Replace 'digital_data' column with 'teethSeen' values
    dataFrame['digital_data'] = rpms
    
    # Convert the DataFrame back to a list of lists format
    return dataFrame #[['time', 'digital_data', 'analog_data']].values.tolist()


def compressData(df, interval):

    times = range(0, int(df['time'].iloc[-1]), interval)
    prevAnalog = df['analog_data'].iloc[0]
    prevDigital = df['digital_data'].iloc[0]
    
    # Select the first entry within each interval
    compressed_df = pandas.DataFrame({'time_interval' : times})



     # Lists to store the compressed values
    analog_data_list = []
    digital_data_list = []

    # Iterate through each interval and find the closest data point
    for currInterval in times:
        # Get all rows within the current interval range
        interval_data = df[(df['time'] >= currInterval) & (df['time'] < currInterval + interval)]
        
        if not interval_data.empty:
            # If data is available within the interval, use the closest data point to the interval start
            closest_row = interval_data.iloc[0]
            currAnalog = closest_row['analog_data']
            currDigital = closest_row['digital_data']
        else:
            # If no data within the interval, use the previous values
            currAnalog = prevAnalog
            currDigital = prevDigital

        # Append the current values to the lists
        analog_data_list.append(currAnalog)
        digital_data_list.append(currDigital)
        
        # Update previous values
        prevAnalog = currAnalog
        prevDigital = currDigital

    # Assign the lists to the DataFrame
    compressed_df['analog_data'] = analog_data_list
    compressed_df['digital_data'] = digital_data_list

    return compressed_df[['time_interval', 'digital_data', 'analog_data']].values.tolist()


#untouched data
print(dataFrame[['time', 'digital_data', 'analog_data']].values.tolist())
print("\n" * 10)

#call the functions
dataFrame = averageAnalog(dataFrame, analogPullRate)
dataFrame = processHallEffect(dataFrame, digitalPullRate)
dataFrame = compressData(dataFrame, math.gcd(analogPullRate, digitalPullRate))

#compressed dataSet
print(dataFrame)
