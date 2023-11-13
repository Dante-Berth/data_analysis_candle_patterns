import pandas as pd
from typing import Optional
def concatenate_multiple_dataframes(X:list[pd.DataFrame]):
    raise "To Be Implemented"
def opener_dataframe(PATH:str="../Data/ETHUSDT-5m.zip")->pd.DataFrame:
    """
    Function used to open and to process the dataframe
    Args:
        PATH (str): PATH

    Returns:
        a panda.DataFrame is returned
    """

    if PATH[-7:] == "csv.zip":
        df = pd.read_csv(PATH, delimiter=';')
    elif PATH[-4:]==".pkl":
        df = pd.read_pickle(PATH)
    else:
        df = pd.read_csv(PATH)

    df.columns = df.columns.str.lower()
    print(df.columns)
    if "Unnamed: 0" in df.columns:
        df = df.drop("Unnamed: 0",axis=1)
    if "open_date" in df.columns:
        df["open_date"] = pd.to_datetime(df["open_date"], errors='coerce').dt.strftime('%Y-%m-%d %H:%M:%S')
        df["open_time"] = pd.to_datetime(df['open_date'], format='%d.%m.%Y %H:%M:%S.%f', errors='coerce').astype('int64')/10**6
    elif "gmt time" in df.columns:
        df['open_date'] = pd.to_datetime(df['gmt time'], format='%d.%m.%Y %H:%M:%S.%f', errors='coerce').dt.strftime('%Y-%m-%d %H:%M:%S')
        df["open_time"] =  pd.to_datetime(df['gmt time'], format='%d.%m.%Y %H:%M:%S.%f', errors='coerce').astype('int64')/10**6
        df = df.drop("gmt time", axis=1)
    else:
        pass

    try:
        if "close" not in df.columns:
            print("The data frame does not contain the close price, created thanks to open price")
            if "open_price" in df.columns:
                df["close"] = df["open_price"].shift(-1)
            elif "open" in df.columns:
                df["close"] = df["open"].shift(-1)
    except:
        pass
    try:
        if "open" in df.columns:
            df['open_price'] = df['open']
            df = df.drop("open",axis=1)
    except:
        pass

    #check if nan values are in the dataframe
    nan_values = df.values[df.isna()]
    if len(nan_values)==0:
        print("There is no nan values")
    else:
        print("There is nan values")
    df["open_date"] = pd.to_datetime(df["open_date"])
    return df

def filter_dataframe_by_date_range(dataframe:pd.DataFrame,begin_date:Optional[str]=None,end_date:Optional[str]=None):
    """
    Args:
        dataframe (pd.Dataframe): the dataframe to be filtered
        begin_date (str or None): the starting date, or None if not specified
        end_date (str or None): the ending date, or None if not specified

    Returns:

    """
    if begin_date is not None and end_date is not None:
        df = dataframe[(dataframe['open_date'] >= begin_date) & (dataframe['open_date'] <= end_date)]
    elif begin_date is not None:
        df = dataframe[(dataframe['open_date'] >= begin_date)]
    elif end_date is not None:
        df = dataframe[(dataframe['open_date'] <= end_date)]
    else:
        df = dataframe
    return df.reset_index(drop=True)

if __name__ == "__main__":
    PATH = "../Data/binance-ETHUSDT-5m.pkl"
    df = opener_dataframe(PATH)
    df = filter_dataframe_by_date_range(df,begin_date="2023-04-03",end_date="2023-05-06")
    print(df.head())
    print(df.columns)