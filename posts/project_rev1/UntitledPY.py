import pandas as pd

# encoding에 대해 찾아보기
df = pd.read_csv('data/crime.csv', encoding='EUC-KR')
crime=df.copy()
crime = crime.rename(columns=crime.iloc[0])
crime = crime.drop([0])
crime.rename(columns={'시점':'year','범죄발생요일별(1)':'day'})
crime.head(3)
