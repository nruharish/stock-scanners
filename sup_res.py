import pandas as pd


def sup_res(file):
    df = pd.read_csv(file)
    print(sr_for_lows(df, 15) + sr_for_highs(df, 15))


def sr_for_lows(df, rolling_window_size):
    df1 = df[['Date',  'Open Price', 'High Price',
              'Low Price',  'Close Price', 'Total Traded Quantity']]
    df1['Agg Low Price'] = df1['Low Price'].rolling(rolling_window_size).min()
    sup_res = df1['Agg Low Price'].value_counts()
    top_sup_res = sup_res[sup_res == rolling_window_size]
    return [items[0] for items in top_sup_res.iteritems()]


def sr_for_highs(df, rolling_window_size):
    df1 = df[['Date',  'Open Price', 'High Price',
              'Low Price',  'Close Price', 'Total Traded Quantity']]
    df1['Agg High Price'] = df1['High Price'].rolling(
        rolling_window_size).max()
    sup_res = df1['Agg High Price'].value_counts()
    top_sup_res = sup_res[sup_res == rolling_window_size]
    return [items[0] for items in top_sup_res.iteritems()]


if __name__ == "__main__":
    sup_res('TATASTEEL.CSV')
