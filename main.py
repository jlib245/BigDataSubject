import pandas as pd


dataset = '광주광역시_시내버스 정류소별 이용객 현황_20240101_with_utf-8.csv'

df = pd.read_csv(dataset)
print(df.head())