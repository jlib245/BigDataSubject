import pandas as pd

# 데이터 불러오기
file_path = "DataSet\\bus_stops_with_coordinates.csv"  # 파일 경로 수정
data = pd.read_csv(file_path)

# '권종' 컬럼에서 '어린이'만 필터링
고

# 결과 확인
print(child_data.head())

# 필터링된 데이터 저장
child_data.to_csv("DataSet\child_only_data.csv", index=False)
print("어린이 데이터가 'child_only_data.csv'에 저장되었습니다.")
