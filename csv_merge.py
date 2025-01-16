#merge multiple csvs on a single key
import pandas as pd

#input data field to merge values on
key = ''

#input file name/path as string
df1 = pd.read_csv("")
df2 = pd.read_csv("")
result = pd.merge(df1, df2, on=key)
result.to_csv("")