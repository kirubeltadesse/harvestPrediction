import pandas as pd

def cleanup(df, onehot=True):
    # droping the unknow values
    df = df.dropna()

    # Putting the index as a column
    df = df.reset_index()
    #     df['Year'] = pd.DatetimeIndex(df['index']).year
    df['Month'] = pd.DatetimeIndex(df['index']).month
    df['Day'] = pd.DatetimeIndex(df['index']).day

    # The "stage" column is really categorical, not numeric. so covert that to a one-hot:
    if(onehot):
        Stage = df.pop("stage")
        df['Bud'] = (Stage == 1) *1.0
        df['Bloom'] = (Stage == 2) *1.0
        df['Veraison'] = (Stage == 3) *1.0
        df['Harvest'] = (Stage == 4)*1

    df = df.drop('index',axis=1)
    df = df.drop('type', axis=1)
    return df