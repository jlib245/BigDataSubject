import chardet

input_file = "DataSet\\광주광역시 서구_이동형 주차단속 현황_20221231.csv"  # 변환할 파일명
output_file = "DataSet\\주정차.csv"  # 저장할 파일

print(f"파일이 {output_file}로 UTF-8로 저장되었습니다.")
# 파일 인코딩 감지
with open(input_file, 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    print(f"감지된 인코딩: {result['encoding']}")

# 해당 인코딩으로 변환


with open(input_file, 'r', encoding=result['encoding']) as infile:
    content = infile.read()

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write(content)

print(f"파일이 {output_file}로 UTF-8로 저장되었습니다.")
