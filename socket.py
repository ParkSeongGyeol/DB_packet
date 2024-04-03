import socket

# 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 수신할 호스트와 포트 설정
host = '0.0.0.0'  # 모든 IP 주소로부터 수신
port = 3306      # 예시 포트 번호

# 소켓 바인딩
sock.bind((host, port))

# 패킷 수신 및 처리
while True:
    data, addr = sock.recvfrom(1024)  # 최대 1024바이트의 데이터 수신
    packet_data = data.decode()        # 바이트를 문자열로 디코딩
