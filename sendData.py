import os
import pymysql
import time

# 패킷 데이터를 받는 함수
def receive_packet_data():
    # 패킷 데이터를 받는 코드를 여기에 작성하세요.
    # 이 예제에서는 임의의 데이터를 반환합니다.
    return {
        "vehicle_number": 1,
        "license_plate": "12가 3456",
        "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }

# 파일에 데이터를 추가하는 함수
def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(str(data) + "\n")

# MariaDB에 데이터를 입력하는 함수
def insert_into_db(data):
    conn = None
    try:
        # MariaDB 연결 설정
        conn = pymysql.connect(
            host="192.168.45.135",
            user="root",
            password="Q!w2e3r4",
            db="test",
            charset='utf8mb4'
        )

        cur = conn.cursor()
        # 테이블이 있는지 확인하고 없으면 생성
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tabel1 (
                vehicle_number INT,
                license_plate VARCHAR(255),
                time TIMESTAMP
            )
        """)

        # SQL 쿼리를 작성하여 데이터를 DB에 입력
        cur.execute("INSERT INTO tabel1 (vehicle_number, license_plate, time) VALUES (%s, %s, %s)", (data["vehicle_number"], data["license_plate"], data["time"]))

        conn.commit()
    except Exception as e:
        print(f"Error connecting to MariaDB: {e}")
    finally:
        if conn:
            conn.close()
# 메인 함수
def main():
    while True:
        data = receive_packet_data()
        append_to_file("request.txt", data)

        if os.path.exists("request.txt"):
            os.rename("request.txt", "new_request.txt")

            with open("new_request.txt", 'r') as file:
                lines = file.readlines()
                for line in lines:
                    db_data = eval(line.replace('\n', ''))
                    insert_into_db(db_data)

            os.remove("new_request.txt")

if __name__ == "__main__":
    main()
