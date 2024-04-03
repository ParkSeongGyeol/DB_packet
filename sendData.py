import os
import pymysql

# 데이터베이스 연결 설정
db = pymysql.connect(host='localhost', user='user', password='password', db='your_db')

def write_to_file(data, filename='request.txt'):
    mode = 'a' if os.path.exists(filename) else 'w'
    with open(filename, mode) as file:
        file.write(data + '\n')

def read_from_file(filename='request.txt'):
    with open(filename, 'r') as file:
        return file.readlines()

def write_to_db(data_list):
    cursor = db.cursor()
    for data in data_list:
        # SQL 쿼리 실행 (예시)
        cursor.execute('INSERT INTO your_table (column) VALUES (%s)', (data,))
    db.commit()

def process_data():
    # 1. 패킷을 통해 데이터를 입력받는다고 가정
    packet_data = 'some_data_received'

    # 2. request.txt 파일에 데이터를 저장
    write_to_file(packet_data)

    # 3. DB에 내용을 저장하기 위해 파일 이름 변경 및 DB에 데이터 입력
    if os.path.exists('request.txt'):
        os.rename('request.txt', 'new_request.txt')
        data_to_db = read_from_file('new_request.txt')
        write_to_db(data_to_db)
        os.remove('new_request.txt')

# 데이터 처리 실행
process_data()
