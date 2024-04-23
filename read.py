import pandas as pd
df = pd.read_csv('myfile.csv', sep=',', header=None)
print(df.values)
