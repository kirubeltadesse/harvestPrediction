import pandas as pd
import numpy as np
import requests, json, glob

path = r'C:/Users/ktadesse/Google Drive/research/VACCINE/Research Direction/Napa Valley/'
filenames = glob.glob(path +"*/rainfall.csv")

# big_fame = pd.concat([pd.read_csv(f, names=['dates', 'inches']) for f in glob.glob(path +"*/rainfall.csv")],
#                     ignore_index=True, sort=Ture)
df_rain = pd.concat([pd.read_csv(f, names=['dates','inches']) for f in glob.glob(path +"*/rainfall.csv")])
df_stages = pd.concat([pd.read_csv(f, names=['dates','types']) for f in glob.glob(path +"*/stages.csv")])

# resetting the date as an index
rain = df_rain.set_index('dates')
stages = df_stages.set_index('dates')

# convering the date to a date datatype
rain.index = pd.to_datetime(rain.index)
stages.index = pd.to_datetime(stages.index)

def cleanup(df, onehot=True):
    # droping the unknow values
    df = df.dropna()

    if('index' not in df.columns):
        df = df.reset_index()

    #     df['Year'] = pd.DatetimeIndex(df['index']).year
    df['Month'] = pd.DatetimeIndex(df['index']).month
    df['Day'] = pd.DatetimeIndex(df['index']).day
    df = df.set_index('index')
    df = df.reset_index(drop=True)


    # The "stage" column is really categorical, not numeric. so covert that to a one-hot:
    if(onehot):
        Stage = df.pop("stage")
        df['Bud'] = (Stage == 1) *1.0
        df['Bloom'] = (Stage == 2) *1.0
        df['Veraison'] = (Stage == 3) *1.0
        df['Harvest'] = (Stage == 4)*1

    #df = df.drop('index',axis=1)
    df = df.drop('type', axis=1)
    return df


# We need to take one type and range of dates
# make a dataframe
# make index date range
# return the dataset of a given datatype
def make_dataset(kind, start, end):
    df = weather_mulit_years(start, end)

    duration = pd.date_range(start, end, freq='D')

    dataset = pd.DataFrame(
        columns=['minTemp', 'maxTemp', 'Eto_values', 'DayPrecip', 'WindSpd', 'DaySolRad', 'rain', 'type', 'stage'])

    start = np.nan

    # going through the 4 types of wine (Sauvignon Blanc, Chardonnay, Merlot, and Cabernet Sauvignon)
    # for kind in set(df_stages['types']):
    DATA = {'Start': stages[stages['types'] == kind].index.tolist(),
            'Stages': [(i % 4) for i in range(stages[stages['types'] == 1].shape[0])]
            # ['Bud', 'Bloom','Veraison', 'Harvest']
            }
    # dataframe with date index and value of stages
    dfs = pd.DataFrame(DATA).set_index('Start')

    # going through each date
    for i in duration.date:
        if i in df.index:
            entry = pd.DataFrame({'minTemp': df.loc[i, 'DayAirTmpMin'],
                                  'maxTemp': df.loc[i, 'DayAirTmpMax'],
                                  'Eto_values': df.loc[i, 'Eto_values'],
                                  'DayPrecip': df.loc[i, 'DayPrecip'],
                                  'WindSpd': df.loc[i, 'DayWindSpdAvg'],
                                  'DaySolRad': df.loc[i, 'DaySolRadAvg']
                                  }, index=[i])

        # adding rain
        if (rain.loc[rain.index.month == i.month]['inches'].empty == True):
            entry['rain'] = 0.00
        else:
            entry['rain'] = rain.loc[rain.index.month == i.month]['inches'][0]

        # adding type
        entry['type'] = kind

        # adding stage
        if (i in dfs.index):
            entry['stage'] = dfs.loc[i][0]
            start = dfs.loc[i][0]
        else:
            # check for the Harevest day
            # if Harvest day has been recorded
            # no need to record the other dates
            if (start == np.int64(3)):
                start = np.nan
                entry['stage'] = start
            else:
                entry['stage'] = start

        dataset = dataset.append(entry, sort=False)

    return dataset