import pandas as pd

def df_from_records(records, time_col="time"):
    if not records:
        return pd.DataFrame()
    df = pd.DataFrame(records)
    df[time_col] = pd.to_datetime(df[time_col])
    return df.sort_values(time_col)