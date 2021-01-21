import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setblocking(False)  # 非阻塞
host = "www.baidu.com"
try:
    client.connect((host, 80))  # 阻塞io，cpu处于空闲
except BlockingIOError as e:
    # do other things
    pass

while 1:
    try:
        client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format("/", host).encode("utf8"))
        print("send success")
        break
    except OSError as e:
        pass
 
data = b""
while 1:
    try:
        d = client.recv(1024)  # 阻塞直到有数据
    except (BlockingIOError, OSError):
        continue
    if d:
        data += d
    else:
        break

data = data.decode('utf8')
print(data)
