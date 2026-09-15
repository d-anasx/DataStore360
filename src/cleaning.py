import dataframe

df = dataframe.df
#deleting duplicated

# df_no_dup = df.drop_duplicates()
# df_no_dup.to_csv('data/processed/store_data.csv')

print(df.isna().sum())

