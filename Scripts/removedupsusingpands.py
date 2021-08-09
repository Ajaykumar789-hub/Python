import pandas as pd
df = pd.read_csv('Employeedata.txt')
print(df)
print("&&&&&&&")
# df_clean=df.drop_duplicates(subset=['id','name'])
df_clean=df.duplicated()
print(df_clean)
# print(df_clean) #to check cleaned file
# df_clean.to_csv('output11.txt',index=False,header=True) #to write cleaned output file