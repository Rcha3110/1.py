import pandas as pd
df= pd.read_csv(r"C:\Users\user\Downloads\Salary_dataset.csv") 
df=df.drop(columns='Unnamed: 0')
df.head(10)
df.isnull().sum()
df.describe()
