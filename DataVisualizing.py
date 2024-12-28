import pandas as pd
import folium

# 데이터 불러오기
file_path = "DataSet\\bus_stops_with_coordinates.csv"  # 파일 경로 수정
bus_data = pd.read_csv(file_path)

file_path = "DataSet\\child_only_accident.csv" 
accident_data = pd.read_csv(file_path)

file_path = "DataSet\\광주광역시_서구_어린이보호구역_20240724.csv"
protect_data = pd.read_csv(file_path)

file_path = "DataSet\\주정차.csv"
parking_data = pd.read_csv(file_path)


# 지도 초기화 (광주광역시 중심 좌표 설정)
map_gwangju = folium.Map(location=[35.1595454, 126.8526012], zoom_start=13)

# 정류소마다 원형 마커 추가
for _, row in bus_data.iterrows():
    if pd.notnull(row["위도"]) and pd.notnull(row["경도"]):
        folium.CircleMarker(
            location=[row["위도"], row["경도"]],
            radius=row["거래건수"] / 20000,  # 거래건수에 비례한 마커 크기
            color="blue",
            fill=True,
            fill_color="blue",
            fill_opacity=0.6,
            popup=f'{row["정류장명"]}: {row["거래건수"]}건'
        ).add_to(map_gwangju)


# 사고지역마다 빨간원
for _, row in accident_data.iterrows():
    if pd.notnull(row["위도"]) and pd.notnull(row["경도"]):
        folium.CircleMarker(
            location=[row["위도"], row["경도"]],
            radius=row["사고"]*4,  # 사고건수에 비례한 마커 크기
            color="red",
            fill=True,
            fill_color="red",
            fill_opacity=0.6,
            popup=f'사고건수: {row["사고"]}건'
        ).add_to(map_gwangju)'''

# 어린이 보호구역역다 빨간원
for _, row in protect_data.iterrows():
    if pd.notnull(row["위도"]) and pd.notnull(row["경도"]):
        folium.CircleMarker(
            location=[row["위도"], row["경도"]],
            radius=30,  
            color="orange",
            fill=True,
            fill_color="orange",
            fill_opacity=0.6,
            popup=f'CCTV설치대수: {row["CCTV설치대수"]}건'
        ).add_to(map_gwangju)

for _, row in parking_data.iterrows():
    if pd.notnull(row["위도"]) and pd.notnull(row["경도"]):
        folium.CircleMarker(
            location=[row["위도"], row["경도"]],
            radius=30,  
            color="violet",
            fill=True,
            fill_color="violet",
            fill_opacity=0.6,
        ).add_to(map_gwangju)



# 결과 저장
map_gwangju.save("gwangju_bus_stops.html")
print("지도가 'gwangju_bus_stops.html'로 저장되었습니다.")