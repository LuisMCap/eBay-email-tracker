import pandas as pd


def save_df(df):
    df.to_csv('tracking.csv', index=False)


def get_original_df():
    old_df = pd.read_csv('tracking.csv')
    return old_df


def filter_data_for_user(df, req_price):
    from_price, to_price = req_price
    req_df = df[(df.price >= from_price) & (df.price <= to_price)].sort_values(by=['price', 'status']).reset_index()
    return req_df
