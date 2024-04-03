import pymysql

# MariaDB 연결 정보
host = 'localhost'
user = 'your_username'
password = 'your_password'
database = 'your_database_name'

# MariaDB 연결
connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             cursorclass=pymysql.cursors.DictCursor)

# 패킷을 통해 데이터를 받아서 처리
packet_data = "Data received from packet"  # 예시로 받은 데이터
process_request(packet_data)
