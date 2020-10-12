import pandas as pd

df_chunk = pd.read_csv('/data/raw_data/gb/1gb_single/data_1gb.csv', chunksize=10**8)
print(df_chunk)

for chunk in df_chunk:
    print(chunk)

# df = pd.concat(df_chunk)
# print(df)