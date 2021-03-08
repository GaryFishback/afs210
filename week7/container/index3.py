import pandas as pd

df = pd.read_csv("items4.csv",sep=",").set_index('ID')

d = dict(zip(df.index,df.values.tolist()))

print(d)

df.plot.bar(x = 'Tour', y = ['Start', 'End'])