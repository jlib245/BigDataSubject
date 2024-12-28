import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# 데이터 불러오기
file_path = "DataSet\\광주광역시_시내버스 정류소별 이용객 현황_20221231_with_utf-8.csv"  # 파일 경로 수정
data = pd.read_csv(file_path)


child_data = data[data["권종"] == "어린이"]

# '정류장명'과 '권종'별로 거래건수 합산 (승하차구분 무시)
grouped_data = data.groupby(['정류장명'], as_index=False).agg({
    '거래건수': 'sum',  # 거래건수를 합산
})


# 결과 저장
grouped_data.to_csv("DataSet\\grouped_bus_data.csv", index=False)
print("거래건수가 합산된 파일이 저장되었습니다.")

file_path = "DataSet\\grouped_bus_data.csv"  # 파일 경로 수정
data = pd.read_csv(file_path)

# Geolocator 초기화
geolocator = Nominatim(user_agent="bus_stop_locator")
# 위도와 경도를 저장할 리스트
latitudes = []
longitudes = []

# 정류장 이름으로 위도, 경도 변환
def get_coordinates(location):
    try:
        loc = geolocator.geocode(location)
        if loc:
            return loc.latitude, loc.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return None, None

for stop in data["정류장명"]:
    lat, lon = get_coordinates(stop)
    latitudes.append(lat)
    longitudes.append(lon)
    print(stop, lat, lon)

# 데이터프레임에 위도, 경도 추가
data["위도"] = latitudes
data["경도"] = longitudes




# 결과 저장
data.to_csv("DataSet\\bus_stops_with_coordinates.csv", index=False)