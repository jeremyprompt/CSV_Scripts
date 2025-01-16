#concatenate csv data into a master csv
import pandas as pd

#input file names/paths as strings
df1 = pd.read_csv("")
df2 = pd.read_csv("")
result = pd.concat([df1,df2], ignore_index=True)
result.to_csv("")