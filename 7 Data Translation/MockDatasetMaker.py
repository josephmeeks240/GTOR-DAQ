import pandas
import numpy
def makeDataset(size):
    # Generate dataset with 100 elements
    data = {
        "time": numpy.random.randint(1, 1000, size=size),
        "digital_data": numpy.random.randint(0, 2, size=size),
        "analog_data": numpy.random.randint(40, 801, size=size)
    }

    dataFrame = pandas.DataFrame(data)
    dataFrame.head()
    # Sort the dataframe by "time" to make it always increasing
    df_sorted = dataFrame.sort_values(by="time").reset_index(drop=True)

    # Convert to text format
    text_data = df_sorted.to_string(index=False, header=False)

    return text_data