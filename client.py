import socket
import time

# 서버 설정: IP 주소와 포트 번호
server_ip = '172.20.10.3'
server_port = 1103

# 소켓 객체 생성 및 설정
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결
def connect_to_server(client_socket, server_ip, server_port):
    connected = False
    attempts = 0
    
    while not connected and attempts < 5:
        try:
            client_socket.connect((server_ip, server_port))
            print(f"서버 {server_ip}:{server_port}에 연결되었습니다.")
            connected = True
        
        except Exception as e:
            print(f"서버에 연결할 수 없습니다. 오류:{e}")
            attempts += 1
            if attempts < 5:
                print("10초 후 다시 시도합니다...")
                time.sleep(10)
                
    if not connected:
        print("서버에 연결하지 못했습니다. 5번 시도 후 종료합니다.")
        client_socket.close()
            
    return connected

# 서버에게 데이터 전송
client_socket.send("안녕하세요, 서버!".encode('utf-8'))

# 서버로부터 데이터 수신
data = client_socket.recv(1024).decode('utf-8')
print(f"서버로부터 받은 데이터: {data}")

# 서버에게 키워드 전송
while True:
    keyword = input("Enter a keyword (type 'quit' to exit): ")
    if keyword == "quit":
        break
    client_socket.send(keyword.encode('utf-8'))
    recv_data = client_socket.recv(1024).decode('utf-8').strip()
    if "No match found" in recv_data:
        print("No data found for the given keyword.")
    else:
        print(f"Data for '{keyword}': {recv_data}")

# 소켓 종료
client_socket.close()
