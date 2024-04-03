import os
import shutil

def process_request(data):
    # 2. request.txt 파일 생성 또는 추가
    with open('request.txt', 'a') as file:
        file.write(data + '\n')

    # 3. new_request.txt로 파일명 변경
    os.rename('request.txt', 'new_request.txt')

    # 4. new_request.txt의 내용을 DB에 입력
    with open('new_request.txt', 'r') as file:
        for line in file:
            plate_text = line.strip()  # 예시로 각 라인의 데이터를 번호판 문자열로 간주
            insert_query = "INSERT INTO car_data (plate_text) VALUES (%s)"
            cursor.execute(insert_query, (plate_text,))
            connection.commit()

    # new_request.txt 파일 삭제
    os.remove('new_request.txt')
