import socket
from servermodule.python_path_config import *

# 서버 설정: IP 주소와 포트 번호
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

server_ip = get_ip_address()
server_port = 1103

# 소켓 객체 생성 및 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((server_ip, server_port))

# 클라이언트 연결 대기
server_socket.listen(1)
print(f"서버가 {server_ip}:{server_port}에서 클라이언트 연결을 대기합니다...")

# 클라이언트 연결 수락
client_socket, client_addr = server_socket.accept()
print(f"클라이언트 {client_addr}가 연결되었습니다.")

# 클라이언트로부터 인사&이름 수신
hello = client_socket.recv(1024).decode('utf-8')
print(f"클라이언트로부터 받은 데이터: {hello}")
cltname = client_socket.recv(1024).decode('utf-8')


# 클라이언트에게 데이터 전송
client_socket.send("안녕하세요, {cltname}!".encode('utf-8'))
client_socket.send(formatted_data.encode('utf-8'))

# 클라이언트로부터 키워드 수신
while True:
    keyword = client_socket.recv(1024).decode('utf-8')
    if keyword == "quit":
        break
    match = excel_data.get(keyword, None)
    if match is None:
        client_socket.send("No match found\n".encode('utf-8'))
    else:
        formatted_data = ', '.join(map(str, match))
        client_socket.send(f"{formatted_data}\n".encode('utf-8'))

# 소켓 종료
client_socket.close()
server_socket.close()
